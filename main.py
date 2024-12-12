import csv
import json
from dataclasses import field

import keyboard
import requests


def main() -> None:
    # this is an entrypoint, DO NOT WRITE ALL CODE HERE !!!


    ...
def fetch_joke(request):
    joke = requests.get("https://official-joke-api.appspot.com/random_joke")
    json_joke = joke.json()
    json_joke_dict = json.loads(json_joke)
    setup_ = json_joke_dict["setup"]
    punchline = json_joke_dict["punchline"]
    print(setup_)
    keyboard.wait("enter")
    print("entre was pressed, continuing...")
    print(punchline)
    with open("jokes_history.csv", "w", newline="") as file:
        writer = csv.writer(file)
        field = ["date", "setup", "punchline"]







if __name__ == "__main__":
    main()
