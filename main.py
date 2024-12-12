import requests
import csv
import os
from datetime import datetime

JOKES_HISTORY = "jokes_history.csv"

def fetch_joke() -> tuple:
    try:
        r = requests.get("https://official-joke-api.appspot.com/random_joke")
        r.raise_for_status()
        j = r.json()

        return j["setup"], j["punchline"]

    except requests.exceptions.RequestException as e:
        print(f"error: {e}")

def save_to_csv(setup: str, punchline: str) -> None:
    with open(JOKES_HISTORY, mode="a", newline="") as f:
        joke_writer = csv.writer(f)
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if not os.path.exists(JOKES_HISTORY):
            joke_writer.writerow(["ts", "setup", "punchline"])
            joke_writer.writerow([ts, setup, punchline])

def main() -> None:
    while True:
        setup, punchline = fetch_joke()
        if not setup:
            print("error while fetching the joke")
            break
        print(f"Here is your joke: \n{setup}")

        input("\nPress Enter to see the punchline...")
        print(f"\n{punchline}")

        save_to_csv(setup, punchline)

        continuer = input("\nWould you like another joke? (yes/no): ").lower()
        if continuer != "yes":
            break

if __name__ == "__main__":
    main()
