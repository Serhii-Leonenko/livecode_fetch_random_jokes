import requests
import os
import csv
import datetime


def main() -> None:
    create_csv()
    get_joke()


def get_joke() -> None:
    while True:
        try:
            request = requests.get(
                "https://official-joke-api.appspot.com/random_joke"
            )
            request_data = request.json()
            print(request_data["setup"])
            input("Press enter to see the punchline ")
            print(request_data["punchline"])
            write_log(request_data)
            res = input("Do u want to see another joke (yes/no) --> ")

            if "no".startswith(res.lower()):
                break
        except Exception:
            print("Whoops something goes wrong, try again")


def create_csv() -> None:
    path = "jokes_history.csv"
    if not os.path.exists(path):
        with open("jokes_history.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Setup", "Punchline"])


def write_log(data: dict) -> None:
    with open("jokes_history.csv", "a") as file:
        writer = csv.writer(file)
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [time, data["setup"], data["punchline"]]
        writer.writerow(row)


if __name__ == "__main__":
    main()
