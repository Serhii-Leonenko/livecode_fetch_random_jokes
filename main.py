import csv
from datetime import datetime

import requests


def get_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        response.raise_for_status()
        joke = response.json()
        setup = joke["setup"]
        punchline = joke["punchline"]
        return setup, punchline
    except requests.RequestException as error:
        print(f"Error with getting joke: {error}")
        return None


def save_joke_to_csv(setup, punchline):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = [timestamp, setup, punchline]

    with open("jokes_history.csv", "w", newline="", encoding="UTF-8") as file:
        fieldnames = ["Timestamp", "Setup", "Punchline"]
        writer = csv.writer(file, delimiter="|")
        writer.writerow(fieldnames)
        writer.writerow(data)


def main() -> None:
    # this is an entrypoint, DO NOT WRITE ALL CODE HERE !!!
    # ToDo remove these comments
    setup, punchline = get_joke()
    save_joke_to_csv(setup, punchline)

    with open("jokes_history.csv", "r", encoding="UTF-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0])


if __name__ == "__main__":
    main()
