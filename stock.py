import requests
from datetime import date, timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
API_KEY = ""
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY,
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = ""
COMPANY_NAME = "Tesla Inc"

response = requests.get(STOCK_ENDPOINT, stock_params)
response.raise_for_status()
response = response.json()
yesterday_closing = response["Time Series (Daily)"][f"{date.today() - timedelta(days=1)}"]["4. close"]
print(yesterday_closing)

day_before = response["Time Series (Daily)"][f"{date.today() - timedelta(days=2)}"]["4. close"]
print(day_before)

diff = abs(float(yesterday_closing)-float(day_before))
print(diff)

percentage_diff = (diff / float(yesterday_closing)) * 100
print(percentage_diff)

if percentage_diff < 5:
    news_response = requests.get(
        "https://newsapi.org/v2/everything?q=Tesla &apiKey=07f8999389db43918f2e086b656d1736").json()
    three_news_response_data = news_response["articles"][:3]
    three_news_response_list = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_news_response_data]
    print(three_news_response_list)
    for x in range(len(three_news_response_list)):
        if yesterday_closing > day_before:
            symbol = "🔺",
        else:
            symbol = "🔻"
        account_sid = ''
        auth_token = ''
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"TESLA {symbol}{round(percentage_diff)}, {three_news_response_list[x]} ",
            from_='+18312986747',
            to='+447578205905'
        )
