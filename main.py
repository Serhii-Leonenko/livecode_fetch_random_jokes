import requests
import csv
from datetime import datetime
import os

FILE_NAME = "jokes_history.csv"


def is_csv_empty(file_path):
    return os.stat(file_path).st_size == 0


def make_request() -> dict:
    request = requests.get("https://official-joke-api.appspot.com/random_joke")
    return request.json()


def display_joke(joke_data) -> None:
    print("Here's your joke:")
    print(joke_data["setup"])

    user_input = input("Press Enter to see the punchline...")
    if user_input == "":
        print(joke_data["punchline"])

    user_input = input("Would you like another joke? (yes/no):")
    if user_input == "yes":
        joke_data = make_request()
        display_joke(joke_data)


def write_joke(joke_data):
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Timestamp",
                "Setup",
                "Punchline"
            ]
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
    display_joke(joke_data)
    write_joke(joke_data)


if __name__ == "__main__":
    main()
