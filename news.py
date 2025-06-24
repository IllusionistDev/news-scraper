import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headlines = []
for article in soup.find_all("h3"):
    headline = article.get_text()
    link = article.find("a")["href"]
    headlines.append({"headline": headline, "link": link})

df = pd.DataFrame(headlines)
df.to_csv("bbc_headlines.csv", index=False)
print("Scraping complete. Saved to bbc_headlines.csv")
