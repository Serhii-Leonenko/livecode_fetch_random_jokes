from service import JokeApiService
import requests # noqa F401

def main() -> None:
    # this is an entrypoint, DO NOT WRITE ALL CODE HERE !!!
    # ToDo remove these comments

    joke_service = JokeApiService()
    joke_service.start()


if __name__ == "__main__":
    main()
