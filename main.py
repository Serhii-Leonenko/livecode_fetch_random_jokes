import requests
from datetime import datetime
import os
import csv

CSV_file = "jokes_history.csv"

def fetch_random_jokes():
    try:
       response = requests.get("https://official-joke-api.appspot.com/random_joke")
       response.raise_for_status()
       jokes = response.json()
       return jokes["setup"], jokes["punchline"]
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None

def save_jokes_history(setup, punchline):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exist = os.path.isfile(CSV_file)

    with open("jokes_history.csv", mode="w",  newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exist:
            writer.writerow(["Timestamp", "Setup", "Punchline"])
        writer.writerow([timestamp, setup, punchline])

def main():
    while True:
        setup, punchline = fetch_random_jokes()
        if setup and punchline:
            print("Your joke:")
            print(setup)
            input("Press Enter to showing punchline")
            print(punchline)
            save_jokes_history(setup,punchline)
        else:
            print("Failed")
        user_input = input("Would you like another joke?(yes/no):").strip().lower()
        if user_input != "yes":
            print("Thanks for using our Random Joke!")
            break


if __name__ == "__main__":
    main()
