from datetime import datetime
import csv
import requests

def write_to_file(list_with_jokes):
    fields = ["timestamp", "setup", "punchline"]

    with open("jokes_history.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(list_with_jokes)

def make_request():
    request = requests.get("https://official-joke-api.appspot.com/random_joke")
    setup = request.json().get("setup")
    punchline = request.json().get("punchline")
    joke_dict = {
        "setup": setup,
        "punchline": punchline
    }
    return joke_dict

def main() -> None:
    user_answer = ""
    list_with_jokes = []

    while user_answer != "no":
        dict_with_jokes = {}
        joke = make_request()

        print(joke.get("setup"))
        input("\nPress enter to see the punchline\n")
        print(joke.get("punchline"))

        dict_with_jokes["setup"] = joke.get("setup")
        dict_with_jokes["punchline"] = joke.get("punchline")
        dict_with_jokes["timestamp"] = datetime.timestamp(datetime.now())
        list_with_jokes.append(dict_with_jokes)

        user_answer = input("\nDo yo want to see another joke? yes/no\n")

    write_to_file(list_with_jokes)
    print("\nHope you had fun with these jokes! See ya soon!")


if __name__ == "__main__":
    main()
