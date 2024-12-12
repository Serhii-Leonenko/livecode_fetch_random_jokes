import csv
from datetime import datetime

def csv_writer(request_setup: str, request_punchline: str) -> None:
    date = datetime.now()
    current_time = date.strftime("%Y-%m-%d %H:%M:%S")

    headers = ["Timestamp", "Setup", "Punchline"]
    row = [current_time, request_setup, request_punchline]

    with open("jokes_history.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerow(row)
