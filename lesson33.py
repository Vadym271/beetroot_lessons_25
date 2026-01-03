import requests
from bs4 import BeautifulSoup
import json

####################################### task 1  ###########################################
url = "https://uk.wikipedia.org/wiki/%D0%A0%D0%BE%D0%B1%D0%BE%D1%82"

headers = {
    "User-Agent": "MyLearningBot/1.0"
}

response = requests.get(url, headers=headers)

text = response.text #decoded text (HTML)
with open("robots.txt", mode = 'w', encoding = 'utf-8') as f:
    f.write(text)

# pure text
soup = BeautifulSoup(response.text, "html.parser")
text = soup.get_text()

with open("robots_text.txt", mode = "w", encoding= "utf-8") as f:
    f.write(text)

################################## task 2 ###########################################
url = "https://api.pullpush.io/reddit/search/comment/"
params = {
    "User-Agent": "MyLearningBot/1.0",
    "subreddit": "python",
    "size": 100,
    "sort": "asc",
    "sort_type": "created_utc"
}

response = requests.get(url, params= params)
data = response.json()

with open("comments.json", mode= "w") as f:
    f.write(json.dumps(data))

################################################ task 3 ##################################################

city = "London"

url = f"https://wttr.in/{city}?format=3"
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print("Unable to get weather information.")
