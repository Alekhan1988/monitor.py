import smtplib
from email.mime.text import MIMEText
import os
import requests
from bs4 import BeautifulSoup
import time

KEYWORDS = ["Appeal to european fans", "FCK PTN"]
NEWS_URLS = [
    "https://www.euronews.com/news/",
    "https://www.ukrinform.ua/rubric-society",
    time.sleep(2)
    "https://www.france24.com/en/europe/",
    "https://www.dw.com/en/top-stories/europe/",
    "https://www.bbc.com/news/world/europe",
    "https://elpais.com/europa/",
    "https://www.corriere.it/esteri/europa/",
    "https://www.politico.eu/news/",
    "https://www.reuters.com/news/archive/europeNews",
    "https://balkaninsight.com/news/",
    "https://polskieradio.pl/",
    "https://www.euronews.com/",
    "https://www.politico.eu/",
    "https://www.dw.com/en/top-stories/europe/",
    "https://www.france24.com/en/europe/",
    "https://www.bbc.com/news/world/",
    "https://www.reuters.com/news/archive/europe",
    "https://euobserver.com/Euractiv",
    "https://brusselsmorning.com/",
    "https://www.eureporter.com/",
    "https://europeannewsroom.com/",
    "https://www.euroweeklynews.com/",
    "https://www.eutimes.net/",
    "https://www.aljazeera.com/where/europe/",
    "https://www.areweeurope.com/",
    "https://www.thelocal.com/",
    "https://www.eurotopics.net/en",
    "https://www.ft.com/world/europe",
    "https://www.eubusiness.com/",
]
EMAIL_TO = "19aggressor88@gmail.com"

# Дані пошти беруться з секретів GitHub Actions
EMAIL_FROM = os.environ['EMAIL_FROM']
EMAIL_PASS = os.environ['EMAIL_PASS']
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def gather_news():
    matched_news = []
    for url in NEWS_URLS:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        for link in soup.find_all("a"):
            text = link.get_text()
            href = link.get("href")
            for kw in KEYWORDS:
                if kw.lower() in text.lower():
                    matched_news.append(f"{text}: {href}")
        time.sleep(2)
    return matched_news

def send_news_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_FROM, EMAIL_PASS)
    server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    server.quit()

if __name__ == "__main__":
        results = gather_news()
if results:
        send_news_email(
        subject="OSINT Monitoring Results",
        body=" ".join(results)
        )
