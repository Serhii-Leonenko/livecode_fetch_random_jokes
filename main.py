import csv
import requests
from datetime import datetime


def random_joke_fetch() -> tuple[str, str] | tuple[None, None]:
    """Function fetches a random joke from the provided API."""
    try:
        response = requests.get(
            "https://official-joke-api.appspot.com/random_joke"
        )
        response.raise_for_status()
        joke = response.json()
        return joke["setup"], joke["punchline"]
    except requests.RequestException as e:
        print(f"Error {e} encountered while joke fetching")
        return None, None


def joke_display(setup: str, punchline: str) -> None:
    """Function displays the joke to the user."""
    print(f"Here's your joke: \n{setup}")
    input("Press Enter to see the punchline...")
    print(f"{punchline}")


def joke_save(timestamp: str, setup: str, punchline: str) -> None:
    """Function saves the joke to the CSV history file."""
    with open(
            "jokes_history.csv", mode="a", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, setup, punchline])


def main() -> None:
    """Main function that combines the joke handling and displaying."""
    try:
        with open(
                "jokes_history.csv", mode="x", newline="", encoding="utf-8"
        ) as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Setup", "Punchline"])
    except FileExistsError:
        pass

    while True:
        setup, punchline = random_joke_fetch()
        if setup and punchline:
            joke_display(setup, punchline)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            joke_save(timestamp, setup, punchline)

        choice = input("Would you like another joke? (yes/no): ")
        if choice != "yes":
            print("Hope you had a good time!")
            break

if __name__ == "__main__":
    main()
