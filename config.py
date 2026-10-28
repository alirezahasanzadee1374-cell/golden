import os

# ==========================================
# توکن‌ها از GitHub Secrets خوانده می‌شوند
# ==========================================
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

# ==========================================
# پارامترهای استراتژی
# ==========================================
EMA_PERIOD = 200
BAND_PERCENT = 0.01
ENTRY_OFFSET = 0.005
WARNING_DISTANCE = 0.02
TREND_LOOKBACK = 20

# ==========================================
# ۱. ۴ ساعته گلدن (SL 5% / TP 10%)
# ==========================================
STRATEGY_4H_GOLDEN = {
    "name": "4H_GOLDEN",
    "label": "۴ ساعته گلدن",
    "interval": "4h",
    "limit": 300,
    "sl_pct": 0.05,
    "tp_pct": 0.10,
    "short": {
        "FILUSDT": 71.4,
        "XRPUSDT": 66.7,
    },
    "long": {
        "LINKUSDT": 77.8,
        "JSTUSDT": 75.0,
        "REZUSDT": 66.7,
    },
}

# ==========================================
# ۲. ۱ ساعته گلدن (SL 5% / TP 10%)
# ==========================================
STRATEGY_1H_GOLDEN = {
    "name": "1H_GOLDEN",
    "label": "۱ ساعته گلدن",
    "interval": "1h",
    "limit": 300,
    "sl_pct": 0.05,
    "tp_pct": 0.10,
    "short": {
        "TKOUSDT": 70.0,
    },
    "long": {
        "PROMUSDT": 77.8,
        "JSTUSDT": 58.8,
        "OGNUSDT": 55.9,
    },
}

# ==========================================
# ۳. ۱ ساعته سیلور (SL 10% / TP 20%)
# ==========================================
STRATEGY_1H_SILVER = {
    "name": "1H_SILVER",
    "label": "۱ ساعته سیلور",
    "interval": "1h",
    "limit": 300,
    "sl_pct": 0.10,
    "tp_pct": 0.20,
    "short": {
        "TKOUSDT": 63.6,
        "DOGEUSDT": 60.0,
        "JASMYUSDT": 58.3,
    },
    "long": {
        "JSTUSDT": 77.8,
        "PROMUSDT": 61.5,
        "OGNUSDT": 52.2,
        "REZUSDT": 52.0,
    },
}

# ==========================================
# ۴. ۱۵ دقیقه گلدن (SL 5% / TP 10%)
# ==========================================
STRATEGY_15M_GOLDEN = {
    "name": "15M_GOLDEN",
    "label": "۱۵ دقیقه گلدن",
    "interval": "15m",
    "limit": 500,
    "sl_pct": 0.05,
    "tp_pct": 0.10,
    "short": {
        "TKOUSDT": 60.6,
    },
    "long": {},
}

# ==========================================
# ۵. ۱۵ دقیقه سیلور (SL 5% / TP 10%)
# ==========================================
STRATEGY_15M_SILVER = {
    "name": "15M_SILVER",
    "label": "۱۵ دقیقه سیلور",
    "interval": "15m",
    "limit": 500,
    "sl_pct": 0.05,
    "tp_pct": 0.10,
    "short": {
        "ALGOUSDT": 50.0,
        "ARBUSDT": 50.0,
        "CFXUSDT": 50.0,
    },
    "long": {
        "TRBUSDT": 51.3,
        "ETHFIUSDT": 52.2,
    },
}

# ==========================================
# ۶. ۱ ساعته برنز (SL 5% / TP 10%) — ۱۵ ارز امن
# ==========================================
STRATEGY_1H_BRONZE = {
    "name": "1H_BRONZE",
    "label": "۱ ساعته برنز",
    "interval": "1h",
    "limit": 500,
    "sl_pct": 0.05,
    "tp_pct": 0.10,
    "short": {
        "ADXUSDT": 50.0,
        "IOUSDT": 56.2,
        "LUNCUSDT": 50.0,
        "SCUSDT": 60.0,
        "RVNUSDT": 57.1,
        "SYNUSDT": 69.2,
        "1000CHEEMSUSDT": 50.0,
        "PORTOUSDT": 64.3,
    },
    "long": {
        "AMPUSDT": 47.4,
        "CVXUSDT": 52.0,
        "INITUSDT": 69.2,
        "MEMEUSDT": 58.3,
        "NMRUSDT": 55.6,
        "OGUSDT": 47.4,
        "TUTUSDT": 58.8,
    },
}

# ==========================================
# ۷. ۴ ساعته سیلور (SL 5% / TP 10%)
# ==========================================
STRATEGY_4H_SILVER = {
    "name": "4H_SILVER",
    "label": "۴ ساعته سیلور",
    "interval": "4h",
    "limit": 500,
    "sl_pct": 0.05,
    "tp_pct": 0.10,
    "short": {
        "AUSDT": 75.0,
        "DOGSUSDT": 75.0,
        "BLURUSDT": 75.0,
        "MOVRUSDT": 75.0,
        "JUVUSDT": 62.5,
        "YFIUSDT": 62.5,
        "AAVEUSDT": 60.0,
        "APTUSDT": 60.0,
        "DYDXUSDT": 60.0,
        "ENSUSDT": 60.0,
        "NMRUSDT": 60.0,
        "NOTUSDT": 60.0,
        "PUNDIXUSDT": 60.0,
        "KAIAUSDT": 60.0,
        "NEXOUSDT": 60.0,
    },
    "long": {
        "1000CHEEMSUSDT": 66.7,
        "VANAUSDT": 83.3,
        "MANAUSDT": 75.0,
        "SANTOSUSDT": 75.0,
        "BANANAUSDT": 66.7,
        "HYPERUSDT": 57.1,
        "BNTUSDT": 57.1,
        "CVXUSDT": 60.0,
        "EIGENUSDT": 60.0,
        "IDUSDT": 60.0,
    },
}

# ==========================================
# ۸. نیم ساعته گلدن (SL 5% / TP 10%) — ۳۶ ارز امن
# ==========================================
STRATEGY_30M_GOLDEN = {
    "name": "30M_GOLDEN",
    "label": "نیم ساعته گلدن",
    "interval": "30m",
    "limit": 500,
    "sl_pct": 0.05,
    "tp_pct": 0.10,
    "short": {
        "2ZUSDT": 50.0,
        "OPUSDT": 55.6,
        "TWTUSDT": 53.3,
        "XTZUSDT": 53.3,
        "FETUSDT": 57.1,
        "API3USDT": 53.8,
        "ARKMUSDT": 50.0,
        "BCHUSDT": 50.0,
        "CELOUSDT": 55.6,
        "CUSDT": 50.0,
        "HOMEUSDT": 66.7,
        "PYTHUSDT": 53.8,
        "SOLUSDT": 50.0,
        "TURBOUSDT": 53.8,
        "XLMUSDT": 54.5,
    },
    "long": {
        "1000SATSUSDT": 53.3,
        "BANANAUSDT": 50.0,
        "BIOUSDT": 50.0,
        "CHRUSDT": 61.5,
        "DEXEUSDT": 68.8,
        "EIGENUSDT": 53.3,
        "ERAUSDT": 50.0,
        "GPSUSDT": 61.1,
        "KAITOUSDT": 50.0,
        "LINEAUSDT": 50.0,
        "MANAUSDT": 66.7,
        "MMTUSDT": 55.6,
        "NEARUSDT": 50.0,
        "ONGUSDT": 50.0,
        "PORTOUSDT": 54.5,
        "RAYUSDT": 53.8,
        "RESOLVUSDT": 60.0,
        "SPELLUSDT": 71.4,
        "USTCUSDT": 69.2,
        "VELODROMEUSDT": 50.0,
        "LAUSDT": 76.9,
    },
}

# ==========================================
# لیست نهایی استراتژی‌ها (فقط برنز و گلدن)
# ==========================================
ALL_STRATEGIES = [
    STRATEGY_1H_BRONZE,
    STRATEGY_30M_GOLDEN,
]
