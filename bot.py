import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import time

# ======= הגדרות מייל =======
EMAIL_USER = "Avivguma12@gmail.com"
EMAIL_PASSWORD = "fxgqtmhqcrszrzyj"  # כאן תכניס את הסיסמה שלך
EMAIL_TO = "avivguma27@gmail.com"

# ======= פונקציה לשליחת מייל =======
def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_TO

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)

# ======= קריאה של רשימת טיקרים =======
with open("tickers.txt", "r") as f:
    tickers = [line.strip() for line in f if line.strip()]

# ======= פונקציה לדוגמה של ניתוח טכני =======
def analyze_ticker(ticker):
    # כאן תכניס את כל ניתוחי הטכני שבנית
    # לדוגמה בדיקה אם המחיר עולה ב-% מסוים בימים האחרונים
    # כרגע מחזיר סימולציה
    return {
        "ticker": ticker,
        "entry_price": 10.5,
        "target_price": 12.3,
        "stop_loss": 9.8,
        "expected_gain": "17%"
    }

# ======= הרצת הבוט =======
opportunities = []
for ticker in tickers:
    result = analyze_ticker(ticker)
    # לדוגמה: אם הצפי רווח מעל 10%, מציג הזדמנות
    gain_percentage = float(result['expected_gain'].replace('%',''))
    if gain_percentage >= 10:
        opportunities.append(result)

# ======= שליחת המייל =======
if opportunities:
    body = "נמצאו הזדמנויות:\n\n"
    for op in opportunities:
        body += f"{op['ticker']}: כניסה {op['entry_price']}, יעד {op['target_price']}, עצירת הפסד {op['stop_loss']}, צפי רווח {op['expected_gain']}\n"
    body += f"\nזמן ניתוח: {datetime.now()}"
    send_email("Swing Bot Opportunities", body)
