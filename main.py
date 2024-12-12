import requests
import csv
from datetime import datetime



def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke = response.json()
        return {"setup": joke["setup"], "punchline": joke["punchline"]}
    except requests.RequestException:
        print("Error fetching joke")
        return None

def save_joke_to_csv_format(timestamp, setup, punchline):
    filename = "jokes_history.csv"
    try:
        with open(filename, "a") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, setup, punchline])
    except Exception:
        print("Error to save joke to file")

def initialize_csv():
    filename = "jokes_history.csv"
    try:
        with open(filename, "x") as file:
            writer = csv.writer(file)
            writer.writerow(["timestamp", "setup", "punchline"])
    except FileExistsError:
        pass

def interact_joke_sesion():
    while True:
        joke = fetch_joke()
        if not joke:
            print("I can't fetch joke")
            break

        print("\nSetup", joke["setup"])
        input("Press Enter to see the punchline...")
        print("Punchline", joke["punchline"])

    #Try to save joke to csv file
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_joke_to_csv_format(timestamp, joke["setup"], joke["punchline"])

    another_joke = input("If u wanna see other joke? (yes/no)?").strip().lower()
    if another_joke != "yes":
        print("Good bye")



def main() -> None:
    initialize_csv()
    interact_joke_sesion()


if __name__ == "__main__":
    main()