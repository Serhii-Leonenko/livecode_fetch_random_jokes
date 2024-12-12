import requests
import csv
import datatime



def fetch_jokes():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    print(response.status_code)
    joke = response.json()
    return joke

def display_jokes(joke):
    if joke:
        print(joke["setup"])
        input("To press Enter for punchline")
        print(joke["punchline"])

def save_jokes_history(joke):
    time_joke = datatime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("jokes_history.csv", "a") as file:
        history = csv.writer(file)
        history.writerow(time_joke,
                         joke["setup"],
                         joke["punchline"])


def main() -> None:
    while True:
        jokes = fetch_jokes()
        if jokes:
            display_jokes(jokes)
            save_jokes_history(jokes)




if __name__ == "__main__":
    main()
