# Python MongoDB Web Scraping Application

## Overview
This project demonstrates how to use Python with MongoDB to collect, process, and store web data using BeautifulSoup and PyMongo.

The application performs:
- Web scraping from public websites
- Data extraction and processing
- MongoDB database insertion
- Weather data collection and storage

---

## Features
- Quote scraping using BeautifulSoup
- Multi-page data collection
- MongoDB integration using PyMongo
- Weather table scraping
- Data storage verification using MongoDB Compass

---

## Technologies Used
- Python
- MongoDB
- PyMongo
- BeautifulSoup4
- lxml
- Requests

---

## Project Structure

![Project Structure](screenshots/project_structure.png)

---

## Application Execution

### Quote Scraper Output
![Quote Output](screenshots/quotes_output.png)

### MongoDB Insert Output
![MongoDB Insert](screenshots/mongodb_insert_output.png)

### Weather Scraper Output
![Weather Output](screenshots/weather_output.png)

---

## MongoDB Results

### Quotes Collection
![Mongo Quotes](screenshots/mongo_quotes_collection.png)

### Weather Collection
![Mongo Weather](screenshots/mongo_weather_collection.png)

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt

### Run Quote Scraper

python quote_scraper/index.py

### Run Weather Scraper

python weather_scraper/weather.py

## Author
Arbutha Durairaj
