import utils


def main() -> None:
    while True:
        # Fetch a random joke
        joke = utils.fetch_joke()
        if joke:
            setup, punchline = joke["setup"], joke["punchline"]
            print(f"Here's your joke:\n{setup}")

            input("\nPress Enter to see the punchline...\n")
            print(f"{punchline}\n")

            utils.save_joke_to_csv(setup, punchline)

            user_input = (
                input("Would you like another joke? (yes/no): ").strip().lower()
            )
            if user_input != "yes":
                break
        else:
            print("Sorry, couldn't fetch a joke at the moment. Try agaim later.")
            break


if __name__ == "__main__":
    main()
