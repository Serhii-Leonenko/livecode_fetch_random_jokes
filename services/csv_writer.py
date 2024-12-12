from datetime import datetime


def csv_writer(request_setup: str, request_punchline: str) -> None:
    with open("jokes_history.csv", "a") as file:

        date = datetime.now()
        current_time = date.strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"Timestamp: {current_time} \n")
        file.write(f"Setup: {request_setup} \n")
        file.write(f"Punchline: {request_punchline} \n")
