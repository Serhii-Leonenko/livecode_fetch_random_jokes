from http.client import responses
from turtledemo.clock import setup

import requests
import csv
import datetime

def get_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        response.raise_for_status()
        joke = response.json()
        return joke["setup"], joke["punchline"]
    except requests.exceptions.RequestException as e:
        print(f"OOPS, error: {e}")


def save_joke_to_csv(timestamp, setup, punchline):
    with open("jokes_history.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows([timestamp, setup, punchline])



def main() -> None:
    print("")
    while True:
        joke = get_joke()
        if not joke:
            print("")
            continue
        setup, punchline = joke
        print("Here's your joke: ")
        print(setup)
        print("Press Enter to see the punchline... ")
        print(punchline)

        timestamp = datetime.now()
        save_joke_to_csv(timestamp, setup, punchline)

        another  = input("Do you want one more joke? (yes/no)" ).strip().lower()
        if another  != "yes":
            print("Buy")
        break



if __name__ == "__main__":
    try:
        with open("jokes_history.csv", mode="x", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(["Timestamp", "Setup", "Punchline"])
    except FileExistsError:
        pass

    main()
