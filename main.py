import requests
import datetime
import csv

def fetch_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        response.raise_for_status()
        joke_data = response.json()
        return joke_data["setup"], joke_data["punchline"]
    except requests.exceptions.RequestException as e:
        print(f"There is an error with fetching a joke - {e}")
        return None, None

def display_a_joke(setup: str, punchline: str) -> None:
    print(f"A joke for you:\n{setup}")
    input(f"To see the punchline press Enter!")
    print(punchline)

def saving_jokes_history(setup: str, punchline: str) -> None:
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    with open("jokes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, setup, punchline])

def get_another_joke():
    while True:
        response = input("Do you want one more joke? yes or no: ").lower()
        if response in ["yes", "no"]:
            return response
        else:
            print("Please respond yes or no")

def main() -> None:
    print("This is random jokes generator!")

    while True:
        setup, punchline = fetch_joke()

        if setup and punchline:
            display_a_joke(setup, punchline)
            saving_jokes_history(setup, punchline)

        if not get_another_joke():
            print("Okay, that's enough jokes for today! Have a nice day!")
            break

        else:
            print("I'm sorry i cannot fetch a joke for some reason")
            break


if __name__ == "__main__":
    main()
