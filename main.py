from random import choice

import requests
import csv
from datetime import datetime


def fetch_random_joke() -> dict | None:
    """
    Fetch a random joke from the Official Joke Api.
    Returns:
        A dict with "setup" and "punchline" if successful, else - None.
    """
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        response.raise_for_status()
        joke = response.json()
        return {
            "setup": joke["setup"],
            "punchline": joke["punchline"]
        }
    except requests.RequestException as e:
        print(f"Error fetching joke: {e}")
        return None

def save_joke_to_csv(
        timestamp: str,
        setup: str,
        punchline: str,
        filename="jokes_history.csv"
):
    """
    Save a joke with a timestamp to a CSV file.
    :param timestamp:
    :param setup:
    :param punchline:
    :param filename:
    """
    try:
        with open(filename, mode="a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, setup, punchline])
    except IOError as e:
        print(f"Error of saving the joke to file: {e}")

def main() -> None:
    """
    Main function to run the joke-fetching app
    """
    while True:
        joke = fetch_random_joke()
        if joke:
            print("\nHere's your joke:")
            print(joke["setup"])
            input("\nPress Enter to see the punchline ...")
            print(joke["punchline"])

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_joke_to_csv(timestamp, joke["setup"], joke["punchline"])

            choice = input("\nWould you like another joke? (yes/no):").strip().lower()
            if choice == "no":
                print("\n Thanks for using this app! Goodbye.")
                break
            else:
                print("\nPlease try again later")

if __name__ == "__main__":
    try:
        with open("jokes_history.csv", mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Setup", "Punchline"])
    except IOError as e:
        print(f"Error initializing CSV file: {e}")

    main()
