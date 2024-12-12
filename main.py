import os.path

import requests
import csv
from datetime import datetime

from exceptions import ResponseError


def main() -> None:
    # this is an entrypoint, DO NOT WRITE ALL CODE HERE !!!
    # ToDo remove these comments

    def get_joke():
        try:
            response = requests.get('https://official-joke-api.appspot.com/random_joke/')

            if not response:
                raise ResponseError
                return

            return response.json()
        except ResponseError as error:
            print(error.message)

    while True:

        joke = get_joke()
        if not joke:
            break
        setup = joke["setup"]
        punchline = joke["punchline"]
        print(f"Here's your joke: \n {setup}")
        input("Press Enter to see the punchline...")
        print(punchline)
        is_exist = os.path.exists("jokes_history.csv")

        if not is_exist:
            with open("jokes_history.csv", 'a') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(
                    ["timestamp", "setup", "punchline"]
                )


        with open("jokes_history.csv", 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(
                [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), setup, punchline]
            )

        answer = input("Would you like another joke? (yes/no):")

        if answer == "yes":
            continue
        if answer == "no":
            break

if __name__ == "__main__":
    main()
