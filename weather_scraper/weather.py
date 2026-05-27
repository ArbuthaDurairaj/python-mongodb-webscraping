import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from datetime import datetime, timezone

# Step 1: Load the page
url = "https://www.weather.gc.ca/canada_e.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")

# Step 2: Locate the table
table = soup.find("table",  class_= "table table-condensed table-hover table-striped")  

# Step 3: Extract headers
headers = [th.text.strip() for th in table.find_all("th")]

# Step 4: Extract rows
rows = []
for tr in table.find_all("tr")[1:]:  # Skip header row
    cells = [td.text.strip() for td in tr.find_all("td")]
    if len(cells) == len(headers):
        row_data = dict(zip(headers, cells))
        row_data["last_modified"] = datetime.now(tz=timezone.utc)
        rows.append(row_data)

client = MongoClient("mongodb://localhost:27017/")
db = client["weatherDB"]
collection = db["canadaWeather"]
collection.insert_many(rows)

print(f"Inserted {len(rows)} records into MongoDB.")