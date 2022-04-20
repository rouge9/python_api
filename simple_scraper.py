from bs4 import BeautifulSoup
# import lxml
import requests


response = requests.get("https://news.ycombinator.com/news")
yc_news = response.text
soup = BeautifulSoup(yc_news, "html.parser")
article_title = soup.find_all(class_="titlelink")
article_link = []
article_text = []
for tag in article_title:
    link = tag.get("href")
    article_link.append(link)
    text = tag.getText()
    article_text.append(text)

article_upvote = [int(upvote.getText().split()[0]) for upvote in soup.find_all(name="span", class_="score")]


# print(article_text)
# print(article_link)
# print(article_upvote)

highest_vote = max(article_upvote)
highest_index = article_upvote.index(highest_vote)
print(article_text[highest_index])
print(article_link[highest_index])



