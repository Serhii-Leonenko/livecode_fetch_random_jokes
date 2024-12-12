import requests
import csv
from datetime import datetime


def fetch_random_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        response.raise_for_status()
        joke_data = response.json()
        return joke_data.get("setup"), joke_data.get("punchline")
    except requests.RequestException as e:
        print(f"Error fetching joke: {e}")
        return None, None


def save_joke_to_csv(timestamp: str, setup: str, punchline: str, filename="jokes_history.csv"):
    try:
        with open(filename, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, setup, punchline])
    except Exception as e:
        print(f"Error saving joke to CSV: {e}")


def main() -> None:
    while True:
        setup, punchline = fetch_random_joke()
        if not setup or not punchline:
            print("Failed")
            break

        print(setup)
        input("")
        print(punchline)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_joke_to_csv(timestamp, setup, punchline)

        another = input("")
        if another == "no":
            break


if __name__ == "__main__":
    main()
