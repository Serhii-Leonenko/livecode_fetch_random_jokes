import requests
import csv
from datetime import datetime
import os


def fetch_random_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        response.raise_for_status()
        joke = response.json()
        return joke.get("setup"), joke.get("punchline")
    except requests.RequestException as e:
        print(f"Error fetching joke: {e}")

def save_joke_to_csv(timestamp, setup, punchline, filename="jokes_history.csv"):
    expected_headers = ["Timestamp", "Setup", "Punchline"]
    try:
        file_exists = os.path.exists(filename)
        with open(filename, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(expected_headers)
            writer.writerow([timestamp, setup, punchline])
    except IOError as e:
        print(f"Error saving joke to file: {e}")

def main() -> None:
    print("Welcome to my random jokes generator !")
    print("Generating jokes for you")

    while True:
        setup, punchline = fetch_random_joke()

        if setup and punchline:
            print(f"Joke: {setup}")
            input("Press Enter to see the punchline")
            print(f"Punchline: {punchline}")

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_joke_to_csv(timestamp, setup, punchline)
        else:
            print("Can't Generate joke at this time. Please try again later!")

        choice = input("Would you like to see another joke? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Goodbye! Hope you had some fun.")
            break


if __name__ == "__main__":
    main()
