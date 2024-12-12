import requests
import csv
from datetime import datetime

JOKES_API_URL = "https://official-joke-api.appspot.com/random_joke"
CSV_FILE = "jokes_history.csv"


def fetch_joke():
    try:
        response = requests.get(JOKES_API_URL)
        response.raise_for_status()
        joke = response.json()
        return joke
    except requests.RequestException as e:
        print(f"Error fetching joke: {e}")
        return None


def save_joke_to_csv(setup, punchline):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = False
    try:
        with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
            file_exists = True
    except FileNotFoundError:
        pass

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Setup", "Punchline", "Timestamp"])
        writer.writerow([setup, punchline, timestamp])
