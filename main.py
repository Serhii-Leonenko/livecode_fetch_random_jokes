import csv

from random_jokes import random_joke


def main() -> None:
    file_name = "joke_history.csv"
    try:
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            field = ["Timestamp", "Setup", "Punchline"]
            row_list = random_joke()
            writer.writerow(field)

            writer.writerows(row_list)
    except IOError:
        print ("Could not read file:", file_name)




if __name__ == "__main__":
    main()
