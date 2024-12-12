import csv
from datetime import datetime

import requests


URL = "https://official-joke-api.appspot.com/random_joke"

def create_csv() -> None:
    with open("jokes_history.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Setup", "Punchline"])


def save_jokes_to_csv(
        timestamp: datetime,
        setup: str,
        punchline: str
) -> None:
    with open("jokes_history.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, setup, punchline])


def fetch_random_joke() -> None:
    command = "yes"
    create_csv()

    while True:
        if command == "yes":
            result = requests.get(URL).json()
            timestamp = datetime.now()
            print(type(timestamp))
            setup = result["setup"]
            punchline = result["punchline"]

            save_jokes_to_csv(timestamp, setup, punchline)

            print("Here's your joke:")
            print(setup)
            input("Press Enter to see the punchline...")
            print(punchline)
            command = input("Would you like another joke? (yes/no): ")
        elif command == "no":
            break



def main() -> None:
    fetch_random_joke()


if __name__ == "__main__":
    main()
