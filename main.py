import requests
import csv
from datetime import datetime
import os

FILE_NAME = "jokes_history.csv"
HEADERS = [
    "Timestamp",
    "Setup",
    "Punchline"
]


def is_csv_empty(file_path: str) -> bool:
    return os.stat(file_path).st_size == 0


def make_request() -> dict:
    request = requests.get("https://official-joke-api.appspot.com/random_joke")
    return request.json()


def write_joke(joke_data: dict) -> None:
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=HEADERS
        )
        if is_csv_empty(FILE_NAME):
            writer.writeheader()
        writer.writerow(
            {
                "Timestamp": time_stamp,
                "Setup": joke_data["setup"],
                "Punchline": joke_data["punchline"]
            }
        )


def main() -> None:
    joke_data = make_request()
    write_joke(joke_data)
    print("Here's your joke:")
    print(joke_data["setup"])

    user_input = input("Press Enter to see the punchline...")
    if user_input == "":
        print(joke_data["punchline"])

    user_input = input("Would you like another joke? (yes/no): ")
    if user_input == "yes":
        joke_data = make_request()
        main()


if __name__ == "__main__":
    main()
