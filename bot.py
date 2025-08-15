import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from bs4 import BeautifulSoup

# ======= הגדרות מייל =======
EMAIL_USER = "avivguma27@gmail.com"
EMAIL_PASSWORD = "fxgqtmhqcrszrzyj"
EMAIL_TO = "Avivguma12@gmail.com"

# ======= פונקציה לשליחת מייל =======
def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_TO
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)

# ======= שליפת רשימת penny stocks מהאינטרנט =======
def get_penny_stocks():
    url = "https://www.nasdaq.com/market-activity/stocks/screener?exchange=nasdaq&market-cap=small&price=under5"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")

    tickers = set()
    for link in soup.find_all("a", href=True):
        if "/market-activity/stocks/" in link['href']:
            symbol = link['href'].split("/")[-1].upper()
            if symbol.isalpha() and len(symbol) <= 5:
                tickers.add(symbol)
    return list(tickers)

# ======= ניתוח טכני פשוט =======
def analyze_ticker(ticker):
    # דוגמה בלבד – פה אפשר לשדרג עם נתוני שוק אמיתיים
    # כרגע נניח שמבצע בדיקה ויש סיכוי טוב לרווח
    import random
    entry_price = round(random.uniform(0.5, 5), 2)
    target_price = round(entry_price * random.uniform(1.1, 1.5), 2)
    stop_loss = round(entry_price * 0.9, 2)
    expected_gain = f"{round((target_price - entry_price) / entry_price * 100, 2)}%"
    return {
        "ticker": ticker,
        "entry_price": entry_price,
        "target_price": target_price,
        "stop_loss": stop_loss,
        "expected_gain": expected_gain
    }

# ======= הפעלת הבוט =======
def main():
    tickers = get_penny_stocks()
    opportunities = []

    for ticker in tickers:
        result = analyze_ticker(ticker)
        gain_percentage = float(result['expected_gain'].replace('%',''))
        if gain_percentage >= 10:
            opportunities.append(result)

    if opportunities:
        body = "נמצאו הזדמנויות:\n\n"
        for op in opportunities:
            body += f"{op['ticker']}: כניסה {op['entry_price']}, יעד {op['target_price']}, עצירת הפסד {op['stop_loss']}, צפי רווח {op['expected_gain']}\n"
        body += f"\nזמן ניתוח: {datetime.now()}"
        send_email("Swing Bot Opportunities", body)

if __name__ == "__main__":
    main()