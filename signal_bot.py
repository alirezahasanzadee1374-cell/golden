"""
ربات سیگنال‌دهنده — همه استراتژی‌ها را جداگانه اسکن می‌کند
از آینه بایننس برای دور زدن خطای 451 استفاده می‌کند
"""

import requests
import pandas as pd
import telebot
from datetime import datetime

from config import ALL_STRATEGIES, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from strategy import calculate_ema, check_signal

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
BINANCE_MIRROR = "https://data-api.binance.vision/api/v3/klines"


def fetch_klines(symbol, interval, limit):
    url = f"{BINANCE_MIRROR}?symbol={symbol}&interval={interval}&limit={limit}"
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        data = r.json()
        df = pd.DataFrame(data, columns=[
            'time', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'qav', 'num_trades', 'taker_base', 'taker_quote', 'ignore'
        ])
        for c in ['open', 'high', 'low', 'close']:
            df[c] = df[c].astype(float)
        df['time'] = pd.to_datetime(df['time'], unit='ms')
        return df
    except Exception as e:
        print(f"خطا {symbol} {interval}: {e}")
        return None


def format_signal(sig):
    emoji = "🔴" if sig['direction'] == 'SHORT' else "🟢"
    dir_fa = "شورت" if sig['direction'] == 'SHORT' else "لانگ"
    return (
        f"{emoji} سیگنال {dir_fa} — {sig['symbol']} ({sig['strategy_label']})\n\n"
        f"وین‌ریت: {sig['win_rate']}%\n"
        f"Entry (Limit): {sig['entry']:.6f}\n"
        f"Stop Loss: {sig['sl']:.6f}\n"
        f"Take Profit: {sig['tp']:.6f}\n"
        f"فاصله تا EMA200: {sig['distance']*100:.2f}%\n\n"
        f"⚠️ خودت سفارش لیمیت باز کن"
    )


def scan_strategy(strategy):
    symbols = list(strategy['short'].keys()) + list(strategy['long'].keys())
    signals = []
    for symbol in symbols:
        df = fetch_klines(symbol, strategy['interval'], strategy['limit'])
        if df is None or len(df) < 250:
            continue
        df['ema200'] = calculate_ema(df)
        idx = len(df) - 2
        sig = check_signal(df, idx, strategy, symbol)
        if sig:
            signals.append(sig)
    return signals


def main():
    print(f"[{datetime.now()}] شروع اسکن...")
    all_signals = []
    for strategy in ALL_STRATEGIES:
        print(f"  اسکن {strategy['name']}...")
        signals = scan_strategy(strategy)
        all_signals.extend(signals)
        for sig in signals:
            try:
                bot.send_message(TELEGRAM_CHAT_ID, format_signal(sig), parse_mode=None)
            except Exception as e:
                print(f"خطا در ارسال: {e}")

    if not all_signals:
        try:
            bot.send_message(TELEGRAM_CHAT_ID, "✅ بررسی شد — سیگنالی نبود")
        except Exception as e:
            print(f"خطا: {e}")
        print("سیگنالی نبود.")
    else:
        print(f"{len(all_signals)} سیگنال ارسال شد.")


if __name__ == "__main__":
    main()
