"""
منطق خالص استراتژی — بدون تلگرام، بدون دیتا
"""

import pandas as pd
from config import (
    EMA_PERIOD, BAND_PERCENT, ENTRY_OFFSET,
    WARNING_DISTANCE, TREND_LOOKBACK
)

def calculate_ema(df):
    return df['close'].ewm(span=EMA_PERIOD, adjust=False).mean()


def get_trend_structure(df, end_idx, lookback=TREND_LOOKBACK):
    if end_idx < lookback:
        return None
    window = df.iloc[end_idx - lookback:end_idx]
    highs = window['high'].values
    lows = window['low'].values
    fh, fl = [], []
    for i in range(2, len(window) - 2):
        if all(highs[i] > highs[i - j] for j in range(1, 3)) and \
           all(highs[i] > highs[i + j] for j in range(1, 3)):
            fh.append(highs[i])
        if all(lows[i] < lows[i - j] for j in range(1, 3)) and \
           all(lows[i] < lows[i + j] for j in range(1, 3)):
            fl.append(lows[i])
    if len(fh) < 2 or len(fl) < 2:
        return None
    if fh[-1] > fh[-2] and fl[-1] > fl[-2]:
        return 'LONG'
    if fh[-1] < fh[-2] and fl[-1] < fl[-2]:
        return 'SHORT'
    return None


def check_confluence(df, end_idx, ema_val, is_short=True):
    band_high = ema_val * (1 + BAND_PERCENT)
    band_low = ema_val * (1 - BAND_PERCENT)
    window = df.iloc[max(0, end_idx - 20):end_idx]

    if is_short:
        avg = (window['open'] - window['close']).abs().mean()
        if avg == 0:
            return False
        big_reds = window[
            (window['close'] < window['open']) &
            ((window['open'] - window['close']) > avg * 1.5) &
            (window['high'] >= band_low) & (window['high'] <= band_high)
        ]
        lh = window[
            (window['high'] > window['high'].shift(1)) &
            (window['high'] > window['high'].shift(-1)) &
            (window['high'] >= band_low) & (window['high'] <= band_high)
        ]
        return len(big_reds) > 0 or len(lh) > 0
    else:
        avg = (window['open'] - window['close']).abs().mean()
        if avg == 0:
            return False
        big_greens = window[
            (window['close'] > window['open']) &
            ((window['close'] - window['open']) > avg * 1.5) &
            (window['low'] <= band_high) & (window['low'] >= band_low)
        ]
        ll = window[
            (window['low'] < window['low'].shift(1)) &
            (window['low'] < window['low'].shift(-1)) &
            (window['low'] <= band_high) & (window['low'] >= band_low)
        ]
        return len(big_greens) > 0 or len(ll) > 0


def check_wick(candle, ema_val, is_short=True):
    if is_short:
        return candle['high'] > ema_val and candle['close'] < ema_val
    return candle['low'] < ema_val and candle['close'] > ema_val


def calculate_levels(ema_val, direction, sl_pct, tp_pct):
    if direction == 'SHORT':
        entry = ema_val * (1 + ENTRY_OFFSET)
        sl = entry * (1 + sl_pct)
        tp = entry * (1 - tp_pct)
    else:
        entry = ema_val * (1 - ENTRY_OFFSET)
        sl = entry * (1 - sl_pct)
        tp = entry * (1 + tp_pct)
    return entry, sl, tp


def check_signal(df, idx, strategy, symbol):
    candle = df.iloc[idx]
    ema = candle['ema200']
    if pd.isna(ema) or ema <= 0:
        return None

    current_price = df.iloc[-1]['close']
    distance = abs(current_price - ema) / ema
    if distance > WARNING_DISTANCE:
        return None

    trend = get_trend_structure(df, idx)
    if trend is None:
        return None

    is_short = symbol in strategy['short']
    is_long = symbol in strategy['long']

    if trend == 'SHORT' and not is_short:
        return None
    if trend == 'LONG' and not is_long:
        return None

    if not check_wick(candle, ema, trend == 'SHORT'):
        return None

    if not check_confluence(df, idx, ema, trend == 'SHORT'):
        return None

    entry, sl, tp = calculate_levels(ema, trend, strategy['sl_pct'], strategy['tp_pct'])
    wr = strategy['short'].get(symbol, 0) if trend == 'SHORT' else strategy['long'].get(symbol, 0)

    return {
        'symbol': symbol,
        'direction': trend,
        'entry': entry,
        'sl': sl,
        'tp': tp,
        'distance': distance,
        'win_rate': wr,
        'strategy_label': strategy['label'],
    }
