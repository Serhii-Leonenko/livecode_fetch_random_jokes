# Random Joke Fetcher

## **Objective**

Build a command-line application in Python that fetches random jokes from
the [Official Joke API](https://official-joke-api.appspot.com/) and displays them to the
user. Additionally, the application should save the history of fetched jokes with a timestamp to a CSV file.

## **Task Description**

You are required to implement a Python script in `main.py` that performs the following:

1. **Fetch Random Jokes:**
    - Use the [requests](https://requests.readthedocs.io/en/latest/) library to make HTTP GET requests to
      `https://official-joke-api.appspot.com/random_joke`.
    - Parse the JSON response to extract the joke's `setup` and `punchline`.

2. **Display Jokes to the User:**
    - Displaying the joke's `setup` and wait for the user to press Enter before showing the `punchline`.
    - After displaying the punchline, ask the user if they want to see another joke with `yes` answer.
    - Continue this process until the user decides to exit with `no` answer.

3. **Save Jokes History:**
    - Record each fetched joke along with the current timestamp to a CSV file named `jokes_history.csv`.
    - The CSV file should have the following columns:
        - `Timestamp` (in format, e.g., `2024-12-01 12:34:56`)
        - `Setup`
        - `Punchline`

4. **Error Handling:**
    - Implement error handling for network requests using try-except blocks.
    - Provide user-friendly messages in case of exceptions (e.g., network issues, API errors).

5. **Code Quality:**
    - Organize your code into functions for better readability and modularity.
    - Use clear and descriptive variable names.
    - Include docstrings where necessary to explain your code.

## **Requirements**

- **Libraries:**
    - `requests` (for making HTTP requests)
    - `csv` (for writing to CSV files)
    - `datetime` (for timestamps)

## **Getting Started**

1. **Fork the Repository:**

    - Click the "Fork" button at the top right of the repository page to create a copy under your GitHub account.

2. **Clone Your Forked Repository:**

   ```bash
   git clone https://github.com/your_username/repository_name.git
   cd repository_name
   ```

3. **Install dependencies**
   ```bash
   pip install requirements.txt
   ```

4. **Implement your solution in the `main.py`**

5. **Test your solution**
   ```bash
   pytest
   ```

6. **Linting your code**
   ```bash
   ruff check .
   ```
7. **Push the solution**
   
   Create PR from your branch to the `main` branch

8. **That's all ) Ask mentor to check your solution**

## **Additional notes**

1. **Example Flow**
   ```
   Here's your joke:
   Why did the chicken cross the road?
   
   Press Enter to see the punchline...
   
   # user press Enter
   
   To get to the other side!
   
   Would you like another joke? (yes/no): yes # user input
   ```

2. **CSV File Format**

   |      Timestamp      |             Setup             |         Punchline          |
      |:-------------------:|:-----------------------------:|:--------------------------:|
   | 2023-10-01 12:34:56 | 	Why did the chicken cross... | 	To get to the other side! |

