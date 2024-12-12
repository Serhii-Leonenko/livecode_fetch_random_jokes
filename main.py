import requests
import csv
from datetime import datetime


def main() -> None:

    while True:
        request = requests.get("https://official-joke-api.appspot.com/random_joke")
        data = [
            ["Timestamp", "Setup", "Punchline"]
        ]

        timestamp = datetime.now()
        setup = request.json()["setup"]
        punchline = request.json()["punchline"]

        data.append([timestamp, setup, punchline])

        print(setup)
        user_input = input("Press enter to see punchline")
        if user_input != "":
            break
        print(punchline)

        user_input = input("Enter \"yes\" or \"no\" to see another joke: ")
        if user_input.lower() != "yes":
            break

        with open("jokes_history.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

    return request


if __name__ == "__main__":
    main()
