import requests
import json


def get_request() -> list:
    r = requests.get("https://official-joke-api.appspot.com/random_joke")
    setup = r.json()["setup"]
    punchline = r.json()["punchline"]
    return [setup, punchline]


def main() -> None:
    while True:
        print("Here's your joke:")

        answer = get_request()

        print(answer[0])

        print("\nPress Enter to see the punchline...")

        user_answer = input("\nWould you like another joke? (yes/no):")

        if user_answer == "":
            print(answer[1])

        if user_answer == "no":
            break


if __name__ == "__main__":
    main()
