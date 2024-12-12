import requests
import csv

def get_request() -> list:
    r = requests.get("https://official-joke-api.appspot.com/random_joke")
    setup = r.json()["setup"]
    punchline = r.json()["punchline"]
    return [setup, punchline]


def main() -> None:
    while True:
        answer = get_request()

        data = [
            ["Timestamp", "Setup", "Punchline"],
            ["", answer[0], answer[1]],
        ]

        with open("jokes_history.csv", mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)

        print("Here's your joke:")
        print(answer[0])

        input("\nPress Enter to see the punchline...")
        print(answer[1])
        user_answer = input("\nWould you like another joke? (yes/no): ")

        if user_answer == "no":
            break







if __name__ == "__main__":
    main()
