import requests
import csv
from datetime import datetime


def fetch_random_joke() -> dict:
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching joke: {e}")
        return None


def save_joke_to_csv(joke: dict) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(
            "jokes_history.csv", "a", newline="", encoding="utf-8"
        ) as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Timestamp", "Setup", "Punchline"])
            writer.writerow([timestamp, joke["setup"], joke["punchline"]])
    except IOError as e:
        print(f"Error saving joke to CSV: {e}")


def display_joke(joke: dict) -> None:
    print("\nJoke:")
    print(joke["setup"])

    input("\nPress Enter to see the punchline...")
    print(f"\n{joke['punchline']}\n")


def main() -> None:
    while True:
        joke = fetch_random_joke()
        if joke:
            display_joke(joke)
            save_joke_to_csv(joke)

            answer = input(
                "Do you want to hear another joke? (yes/no): "
            ).lower()
            if answer != "yes":
                break
        else:
            retry = input("Try again? (yes/no): ").lower()
            if retry != "yes":
                break


if __name__ == "__main__":
    main()
