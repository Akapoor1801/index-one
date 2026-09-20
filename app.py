from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
from pathlib import Path

app = Flask(__name__)
CORS(app)

# ============================================================
# NIFTY 500 STOCKS
# ============================================================

NIFTY_500_STOCKS = [
    "RELIANCE", "TCS", "HDFCBANK", "ICICIBANK", "HINDUNILVR", "INFY", "HDFC",
    "SBIN", "BAJFINANCE", "BHARTIARTL", "KOTAKBANK", "ITC", "LT", "AXISBANK",
    "ASIANPAINT", "HCLTECH", "MARUTI", "SUNPHARMA", "TATAMOTORS", "TITAN",
    "BAJAJFINSV", "WIPRO", "ULTRACEMCO", "ADANIENT", "ADANIGREEN", "NTPC",
    "POWERGRID", "ONGC", "TATASTEEL", "JSWSTEEL", "COALINDIA", "GRASIM",
    "NESTLEIND", "HINDZINC", "VEDL", "BRITANNIA", "CIPLA", "TECHM", "DRREDDY",
    "EICHERMOT", "HEROMOTOCO", "INDUSINDBK", "DIVISLAB", "APOLLOHOSP", "BAJAJ-AUTO",
    "M&M", "SBILIFE", "HDFCLIFE", "ICICIPRULI", "BPCL", "IOC", "GAIL",
    "SHREECEM", "DABUR", "GODREJCP", "MARICO", "PIDILITIND", "HAVELLS",
    "BERGEPAINT", "MCDOWELL-N", "TRENT", "PAGEIND", "JUBLFOOD", "DMART",
    "INDIGO", "INTERGLOB", "IRCTC", "ZOMATO", "NYKAA", "PAYTM", "POLICYBZR",
    "DELHIVERY", "OLA", "SWIGGY", "LICI", "HAL", "BEL", "COCHINSHIP",
    "MAZDOCK", "BDL", "PARAS", "DATAPATTNS", "IDEA", "VODAFONEIDEA",
    "JIOFIN", "RELIANCEPP", "ADANIPORTS", "ADANIPOWER", "ADANITRANS",
    "ADANIWILMAR", "AMBUJACEM", "ACC", "RAMCOCEM", "JKCEMENT", "DALBHARAT",
    "STARCEMENT", "NAVINFLUOR", "SRF", "DEEPAKNTR", "ATUL", "BALAMINES",
    "ALKYLAMINE", "AARTIIND", "GUJFLUORO", "FLUOROCHEM", "PIIND", "SUMICHEM",
    "RALLIS", "BAYERCROP", "UPL", "DHANUKA", "INSECTICID", "BASF", "TATACHEM",
    "TATACONSUM", "VST", "GODFREYPHILL", "GPI", "BLUEDART", "TCI", "ALLCARGO",
    "GATI", "MAHLOG", "CONCOR", "RITES", "IRFC", "RVNL", "IRCON", "RAILTEL",
    "KALYANKJIL", "TANLA", "AFFLE", "NAUKRI", "INDIAMART", "JUSTDIAL",
    "CARTRADE", "EASEMYTRIP", "IXIGO", "MMT", "Yatra", "POLYCAB", "KEI",
    "CROMPTON", "VGUARD", "SYMPHONY", "WHIRLPOOL", "BLUESTARCO", "VOLTAS",
    "DIXON", "AMBER", "HPL", "MIRC", "TTKPRESTIG", "BAJAJELEC", "IFBIND",
    "RATNAMANI", "APLAPOLLO", "JINDALSAW", "SURYAROSNI", "MAHSEAMLES",
    "TUBEINVEST", "WELCORP", "HINDWARE", "CERA", "KAJARIA", "SOMANYCERA",
    "ORIENTBELL", "ASIANTILES", "PRISMJOHN", "GREENPANEL", "CENTURYPLY",
    "GREENPLY", "AEGISCHEM", "CASTROLIND", "GULFOILLUB", "TIDEWATER", "SAFARI",
    "EPL", "UFLEX", "COSMOFIRST", "JINDALPOLY", "XPROINDIA", "DCW", "PCBL",
    "PHILLIPCARB", "BIRLACORPN", "HEIDELBERG", "SANGHIIND", "NCLIND", "SUVEN",
    "JBCHEPHARM", "CAPLIPOINT", "NATCOPHARM", "LUPIN", "AUROPHARMA",
    "TORNTPHARM", "GLENMARK", "ALKEM", "GLAXO", "PFIZER", "SANOFI", "ABBOTT",
    "MEDANTA", "FORTIS", "MAXHEALTH", "NH", "ASTERDM", "KIMS", "YATHARTH",
    "RAINBOW", "KOVAI", "NEULAND", "LASA", "SHILPAMED", "THEMISMED", "TATVA",
    "WINDLAS", "PGHL", "EMAMI", "GODREJIND", "KANSAINER", "JYKLL", "GILLETTE",
    "COLPAL", "LAURUSLABS", "GRANULES", "BIOCON", "SYNGENE", "JUBILANT",
    "LAXMIMACH", "TITAGARH", "TEXRAIL", "BEML", "BHEL", "CUMMINSIND",
    "KIRLOSBROS", "KIRLOSENG", "GREAVESCOT", "SIEMENS", "ABB", "SCHNEIDER",
    "HONEYWELL", "LTTS", "MINDTREE", "LTIM", "PERSISTENT", "COFORGE",
    "MPHASIS", "ZENSARTECH", "SONATSOFTW", "CYIENT", "FIRSTSOURCE", "EXL",
    "WNS", "GENPACT", "ECLERX", "BIRLASOFT", "NEWGEN", "INTELLECT", "MASTEK",
    "SASKEN", "SUBEX", "TRIDENT", "WELSPUNIND", "INDORAMA", "RSWM",
    "VARDMNPOLY", "GOKEX", "NAHARSPING", "ASHIMA", "KPRMILL", "VTL",
    "GARFIBRES", "RPSGVENT", "SAREGAMA", "TIPSMUSIC", "PVRINOX", "CINEPOLIS",
    "SUNDARMFIN", "CHOLAFIN", "BAJAJHLDNG", "BAJAJHIND", "MUTHOOTFIN",
    "MANAPPURAM", "MFSL", "REPCOHOME", "CANFINHOME", "PNBHOUSING", "LICHSGFIN",
    "GICRE", "NIACL", "ICICIGI", "NEWINDIA", "STARHEALTH", "NAVI", "CREDITACC",
    "FIVESTAR", "CAPRI", "MASFIN", "UGROCAP", "SURYODAY", "FINOPB", "FEDFINA",
    "HOMEFIRST", "AAVAS", "RENUKA", "BALRAMCHIN", "BANARISUG", "DWARKESH",
    "DHAMPURSUG", "DAWAT", "CHAMBLFERT", "GNFC", "DEEPAKFERT", "MADRASFERT",
    "PARADEEP", "NFL", "GSFC", "FACT", "BHARATRAS", "BESTAGRO", "NACLIND",
    "PUNJABCHEM", "LINDEINDIA", "SOLARINDS", "AETHER", "CLEAN", "GUJALKALI",
    "TNPETRO", "MANALI", "NOCIL", "BEPL", "MEGH", "GPPL", "JSWINFRA",
    "GMRINFRA", "IRB", "MEP", "KNRCON", "HGINFRA", "PNCINFRA", "ASHOKA",
    "WELENT", "SOBHA", "BRIGADE", "OBEROIRLTY", "DLF", "PHOENIXLTD", "PRESTIGE",
    "GODREJPROP", "MAHLIFE", "SUNTECK", "NCC", "PUNJLLOYD", "SADBHAV",
    "DILIPBUILD", "CAPACITE", "PSPPROJECT", "WALLPAPER", "AKZOINDIA",
    "Nerolac", "SHALIMAR", "INDIGOPNTS", "JKLAKSHMI"
]

NIFTY_500_STOCKS = list(dict.fromkeys(NIFTY_500_STOCKS))


# ============================================================
# MOCK DATA
# ============================================================

MOCK_DATA = {
    "HDFCBANK": {"price": 1850, "pe": 18.5, "pb": 2.1, "roe": 16.5, "div": 1.2},
    "TCS": {"price": 3845, "pe": 28.5, "pb": 5.2, "roe": 22.3, "div": 1.8},
    "INFY": {"price": 2290, "pe": 22.1, "pb": 4.8, "roe": 18.9, "div": 1.5},
    "RELIANCE": {"price": 2850, "pe": 12.5, "pb": 1.8, "roe": 14.2, "div": 2.5},
    "SUNPHARMA": {"price": 850, "pe": 32.1, "pb": 3.5, "roe": 11.2, "div": 0.8},
    "MARUTI": {"price": 12450, "pe": 15.8, "pb": 2.2, "roe": 14.5, "div": 2.1},
    "WIPRO": {"price": 465, "pe": 19.5, "pb": 4.1, "roe": 20.1, "div": 1.3},
    "ICICIBANK": {"price": 1185, "pe": 16.2, "pb": 1.95, "roe": 12.1, "div": 2.3},
    "SBIN": {"price": 680, "pe": 14.8, "pb": 1.2, "roe": 8.1, "div": 2.8},
    "HDFC": {"price": 2950, "pe": 35.2, "pb": 4.5, "roe": 13.2, "div": 1.1},
}


def get_mock_analysis(ticker):
    mock = MOCK_DATA.get(
        ticker.upper(),
        {
            "price": 3000 + (hash(ticker) % 2000),
            "pe": 20 + (hash(ticker) % 20),
            "pb": 2 + (hash(ticker) % 4),
            "roe": 12 + (hash(ticker) % 12),
            "div": 1 + (hash(ticker) % 3)
        }
    )

    price = mock["price"]
    pe = mock["pe"]
    pb = mock["pb"]
    roe = mock["roe"]
    div = mock["div"]

    rsi = 55 + (hash(ticker) % 20)

    tech_score = 55

    if rsi > 70:
        tech_score -= 10
    elif rsi < 30:
        tech_score += 10

    tech_score += hash(ticker) % 10

    fund_score = 50

    if pe < 20:
        fund_score += 15
    elif pe > 40:
        fund_score -= 10

    if pb < 3:
        fund_score += 10

    if roe > 15:
        fund_score += 10

    if div > 1.5:
        fund_score += 5

    overall_score = int(fund_score * 0.6 + tech_score * 0.4)

    if overall_score >= 75:
        verdict = "BUY"
        confidence = "High"
    elif overall_score >= 60:
        verdict = "ACCUMULATE"
        confidence = "Moderate-High"
    elif overall_score >= 45:
        verdict = "HOLD"
        confidence = "Moderate"
    else:
        verdict = "REDUCE"
        confidence = "Low"

    target_12m = price * (
        1.15 if verdict in ["BUY", "ACCUMULATE"] else 0.95
    )

    target_24m = price * (
        1.25 if verdict in ["BUY", "ACCUMULATE"] else 0.85
    )

    return {
        "ticker": ticker,
        "timestamp": datetime.now().isoformat(),

        "verdict": {
            "rating": verdict,
            "confidence": confidence,
            "score": overall_score,
            "sector": "Indian Equity"
        },

        "pricing": {
            "current_price": round(price, 2),
            "target_12m": round(target_12m, 2),
            "target_24m": round(target_24m, 2),
            "52w_high": round(price * 1.2, 2),
            "52w_low": round(price * 0.85, 2)
        },

        "scores": {
            "technical_score": round(tech_score, 1),
            "fundamental_score": round(fund_score, 1),
            "overall_score": overall_score
        },

        "technical_summary": {
            "rsi": round(rsi, 2),
            "macd_status": "Bullish" if hash(ticker) % 2 == 0 else "Bearish",
            "sma_trend": "Uptrend" if hash(ticker) % 2 == 0 else "Downtrend",
            "volume_status": "High" if hash(ticker) % 3 != 0 else "Normal"
        },

        "fundamental_summary": {
            "PE_Ratio": round(pe, 2),
            "PB_Ratio": round(pb, 2),
            "ROE": round(roe, 2),
            "Dividend_Yield": round(div, 2),
            "Current_Ratio": round(2.5 + (hash(ticker) % 10) * 0.1, 2),
            "Debt_Equity": round(0.5 + (hash(ticker) % 5) * 0.2, 2),
            "Interest_Coverage": round(8.5 + (hash(ticker) % 12), 2),
            "Operating_Margin": round(12 + (hash(ticker) % 20), 2),
            "Net_Profit_Margin": round(8 + (hash(ticker) % 15), 2),
            "Asset_Turnover": round(0.8 + (hash(ticker) % 8) * 0.1, 2),
            "EPS": round(15 + (hash(ticker) % 100), 2),
            "Book_Value_Per_Share": round(180 + (hash(ticker) % 500), 2),
            "Price_to_Sales": round(2.5 + (hash(ticker) % 8) * 0.2, 2),
            "Free_Cash_Flow_Million": round(1000 + (hash(ticker) % 5000), 0),
            "Operating_Cash_Flow": round(1500 + (hash(ticker) % 6000), 0)
        },

        "risks": [
            "Market volatility",
            "Sector-specific risks",
            "Macroeconomic factors"
        ]
    }


# ============================================================
# FRONTEND
# ============================================================

@app.route("/")
def index():
    """Serve index.html regardless of Vercel's working directory."""

    index_path = Path(__file__).resolve().parent / "index.html"

    if index_path.exists():
        return index_path.read_text(encoding="utf-8")

    return """
    <!DOCTYPE html>
    <html>
    <body style="font-family:Arial;padding:50px">
        <h1>❌ index.html not found</h1>
        <p>Make sure index.html is in the same folder as app.py.</p>
    </body>
    </html>
    """, 404


# ============================================================
# API
# ============================================================

@app.route("/api/stocks")
def get_stocks():
    return jsonify({
        "stocks": NIFTY_500_STOCKS
    })


@app.route("/api/dashboard/<ticker>")
def get_dashboard(ticker):

    ticker = (
        ticker
        .upper()
        .strip()
        .replace(".NS", "")
        .replace(".BO", "")
    )

    if ticker not in NIFTY_500_STOCKS:
        return jsonify({
            "error": f"Stock '{ticker}' not found in database"
        }), 404

    return jsonify(get_mock_analysis(ticker))


@app.route("/api/health")
def health_check():
    return jsonify({
        "status": "Server is running!",
        "stocks": len(NIFTY_500_STOCKS)
    })


# ============================================================
# LOCAL DEVELOPMENT
# ============================================================

if __name__ == "__main__":
    print("=" * 70)
    print("  Equity Research Dashboard")
    print("  NSE/BSE Stock Coverage")
    print("=" * 70)
    print(f"Database: {len(NIFTY_500_STOCKS)} stocks loaded")
    print("Server: http://localhost:5000")
    print("=" * 70)

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        use_reloader=False
    )
