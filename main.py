import requests
from services.joke_request import get_headers
from services.csv_writer import csv_writer


def main() -> None:

    while True:
        joke_request = requests.get("https://official-joke-api.appspot.com/random_joke")
        headers = get_headers(joke_request)
        request_setup, request_punchline = headers

        print("Here's your joke:")
        print(request_setup, "\n")

        user_input = input("Press Enter to see the punchline... ")

        if user_input == "":
            print(request_punchline, "\n")

        user_input = input("Would you like another joke? (yes/no): ")

        csv_writer(request_setup, request_punchline)

        if user_input.lower() == "yes":
            pass
        elif user_input.lower() == "no":
            break


if __name__ == "__main__":
    main()
