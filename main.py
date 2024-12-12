import requests
import csv
from datetime import datetime
from ast import literal_eval as le


def main() -> None:
    # this is an entrypoint, DO NOT WRITE ALL CODE HERE !!!
    # ToDo remove these comments
    headers = ["Name", "Birthday", "Height"]

    with open("jokes_hostory.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        while True:
            try:
                r = requests.get("https://official-joke-api.appspot.com/random_joke")
            except:
                print()
            response = le(r.text)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # print(timestamp)
            setup = response["setup"]
            punchline = response["punchline"]
            print(setup)
            input("press button... ")
            print(punchline)
            writer.writerow([str(timestamp), str(setup), str(punchline)])
            wait = input("continue? yes/no: ")
            if wait == "no":
                break


if __name__ == "__main__":
    main()
