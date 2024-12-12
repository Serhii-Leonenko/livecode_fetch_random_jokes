import requests
from setuptools import setup


def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            joke = response.json()
            return joke
        else:
            print("Error:", response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


def main() -> None:
    jokes = get_joke()
    print(jokes["setup"])


if __name__ == "__main__":
    main()
