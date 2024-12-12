import csv
from datetime import datetime

import requests
from requests import JSONDecodeError
from requests.exceptions import MissingSchema


def get_joke(address: str) -> dict:
    try:
        response = requests.get(address)
        try:
            return response.json()
        except JSONDecodeError as e:
            print(e)
    except MissingSchema as e:
        print(e)


def save_joke(joke: dict) -> None:
    try:
        with open("jokes_history.csv", "a", newline="") as csvfile:
            fieldnames = ["Timestamp", "Setup", "Punchline"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({
                "Timestamp": datetime.now(),
                "Setup": joke.get("setup", "Error get setup"),
                "Punchline": joke.get("punchline", "Error get punchline"),
            })
    except (PermissionError, IOError) as e:
        print("Can't save joke:")
        print(e)


def display_jokes(address: str) -> None:
    while True:
        joke = get_joke(address)

        if not joke:
            print("Sorry, can't get jokes")
            break

        setup = joke.get("setup")
        punchline = joke.get("punchline")

        if not setup or not punchline:
            print("Something went wrong")
            break

        save_joke(joke)
        print("Here's your joke:")
        print(setup)

        while input("Press enter to see the punchline") != "":
            continue

        print(punchline)

        while (user_input := input(
            "If you want to see another joke print yes, else no: "
        )) not in ("yes", "no"):
            continue
        if user_input == "no":
            print("Bye")
            break


def main() -> None:
    address = "https://official-joke-api.appspot.com/random_joke"
    display_jokes(address)


if __name__ == "__main__":
    main()
