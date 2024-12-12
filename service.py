import os
from datetime import datetime

import requests
import csv

from exceptions import ResponseError


class JokeApiService:
    def __init__(self) -> None:
        self.url = "https://official-joke-api.appspot.com/random_joke/"

    def get_joke(self) -> dict | None:
        try:
            response = requests.get(self.url)

            if not response:
                raise ResponseError
                return

            return response.json()
        except ResponseError as error:
            print(error.message)

    def start(self) -> None:
        while True:

            joke =self.get_joke()
            if not joke:
                break
            setup = joke["setup"]
            punchline = joke["punchline"]
            print(f"Here's your joke: \n {setup}")
            input("Press Enter to see the punchline...")
            print(punchline)
            is_exist = os.path.exists("jokes_history.csv")

            if not is_exist:
                with open("jokes_history.csv", "a") as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(
                        ["timestamp", "setup", "punchline"]
                    )

            with open("jokes_history.csv", "a") as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(
                    [datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                     setup,
                     punchline]
                )

            answer = input("Would you like another joke? (yes/no):")

            if answer == "yes":
                continue
            if answer == "no":
                break
