import csv
import os
from unittest import mock

import pytest
from freezegun import freeze_time

import main


@pytest.fixture(autouse=True)
def remove_jokes_history():
    if os.path.exists("jokes_history.csv"):
        os.remove("jokes_history.csv")
    yield
    if os.path.exists("jokes_history.csv"):
        os.remove("jokes_history.csv")


@freeze_time("2024-12-01 01:01:01")
@mock.patch("main.requests.get")
def test_main(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "setup": "Why did the chicken cross the road?",
        "punchline": "To get to the other side!",
    }

    with mock.patch("builtins.input", side_effect=["", "no"]):
        main.main()

    assert os.path.exists(
        "jokes_history.csv"
    ), "The file 'jokes_history.csv' does not exist."

    with open("jokes_history.csv", "r") as f:
        reader = csv.reader(f)

        expected_headers = ["setup", "punchline", "timestamp"]
        headers = next(reader)
        headers = [header.strip().lower() for header in headers]

        for expected_header in expected_headers:
            assert (
                expected_header in headers
            ), f"The header '{expected_header}' is not in the file."

        row = next(reader)
        assert (
            "2024-12-01 01:01:01" in row
        ), "The timestamp is not in the file or incorrect format"
        assert (
            "Why did the chicken cross the road?" in row
        ), "The setup 'Why did the chicken cross the road?' is not in the file."
        assert (
            "To get to the other side!" in row
        ), "The punchline 'To get to the other side!' is not in the file."
