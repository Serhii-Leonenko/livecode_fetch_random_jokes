import csv
import datetime
import requests
import os


def get_joke() -> str:
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        setup = response.json().get("setup")
        punchline = response.json().get("punchline")
        return setup, punchline
    except requests.RequestException:
        print("Error")


def save_joke_to_scv(time_joke: datetime, setup: str, punchline: str) -> None:
    file_name = "jokes_history.csv"
    file_exists = os.path.isfile(file_name)

    with open(file_name, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Setup", "Punchline"])
        writer.writerow([time_joke, setup, punchline])


def print_joke() -> None:
    setup, punchline = get_joke()
    print(f"Here's your joke:\n{setup}")
    input("Press Enter to see the punchline...")
    print(f"{punchline}\n")
    time_joke = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_joke_to_scv(time_joke, setup, punchline)


def main() -> None:
    while True:
        print_joke()
        user_answer = input("Would you like another joke? (yes/no): ")
        if user_answer.lower() == "no":
            break


if __name__ == "__main__":
    main()
