import html
import os
import requests
import smtplib
import http

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_FOR_NEWS = "f101d01a19e744738fa5fb1524107777"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "0HNFCF3B2KIZZ4P8",
}
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# url = ,params=parameters
response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_data = float(yesterday_data["4. close"])

# print(yesterday_closing_data)
date_list = [key for (key, value) in data.items()]


the_Day_before = data_list[1]
the_Day_before_closing_data = float(the_Day_before["4. close"])
# print(the_Day_before_closing_data)



difference = abs(yesterday_closing_data - the_Day_before_closing_data)
# print(difference)

difference_percent = (difference / yesterday_closing_data) * 100
# print(difference_percent)

# if difference_percent > 5:
#     print("Get news")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if difference_percent > 3:

    parameters_for_news = {
        "q": COMPANY_NAME,
        "from": date_list[1],
        "apiKey": API_KEY_FOR_NEWS,

    }
    r = requests.get("https://newsapi.org/v2/everything",params=parameters_for_news)
    r.raise_for_status()
    articles = r.json()["articles"]
    three_articles = articles[:3]
    if the_Day_before_closing_data > yesterday_closing_data:

        articles_message = [f"Subject: 🔺{int(difference_percent)} \n\nHeadline: {articles['title']} Description: {articles['description']}" for articles in three_articles]
    else:
        articles_message = [f"Subject: 🔻{int(difference_percent)} \n\nHeadline: {articles['title']} Description: {articles['description']}" for articles in three_articles]

html.unescape(articles_message)




## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login('robelgedamu92@gmail.com', password='rouge12roba')
connection.sendmail(from_addr="robelgedamu92@gmail.com", to_addrs="robelgedamu92@gmail.com", msg=articles_message)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
