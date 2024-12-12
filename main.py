from datetime import datetime
import requests
import csv


def main() -> None:
    while True:
        print("Best joke for you:")
        r = requests.get("https://official-joke-api.appspot.com/random_joke")
        joke = r.json()
        print(joke.get("setup"))
        input("Press enter to continue")
        print(joke.get("punchline"))

        csvfile = open('jokes_history.csv', 'a', newline='', encoding='utf-8')

        c = csv.writer(csvfile)

        c.writerow(['Timestamp', 'Setup', 'Punchline'])
        date = datetime.now()
        data = [[str(date), joke.get("setup"), joke.get("punchline")]]
        for item in data:
            c.writerow(item)
        csvfile.close()
        next_joke = input("Do you want new joke? Answer: yes/no")
        if next_joke == "no":
            break
        elif next_joke != "yes":
            print("Please answer: yes/no")


if __name__ == "__main__":
    main()
