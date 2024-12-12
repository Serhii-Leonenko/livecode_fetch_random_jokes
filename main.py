import requests
import csv
from requests import RequestException

def get_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")

        return response.json()
    except RequestException:
        print("Oops, try again later")
        return

# def save_joke_to_csv_file(setup, punchline):
#     with open("jokes_history.csv", "a", newline="") as file:
#         fieldnames = ["Timestamp", "Setup", "Punchline"]
#         writer = csv.writer(file)
#
#         writer.writerow(fieldnames)
#         writer.writerows()

def main() -> None:
    while True:
        joke = get_joke()

        print("\nHere's your joke:")
        print(joke["setup"])
        input("\nPress Enter to see the punchline...")
        print(f"\n{joke["punchline"]}")

        # save_joke_to_csv_file(joke["setup"], joke["punchline"])

        another_one_joke = input("Would you like another joke? (yes/no): ").lower()
        if another_one_joke != "yes":
            break


if __name__ == "__main__":
    main()
