#!/usr/bin/env python3
import requests

URL = "https://opentdb.com/api.php?amount=3&category=9&difficulty=easy&type=boolean"

def main():
    # data will be a python dictionary rendered from your API link's JSON!
    data = requests.get(URL).json()
    # display the question
    print(f"Question - {data['results'][0]['question']}")
    # display the answers
    print(f"Correct answer - {data['results'][0]['correct_answer']}")
    print(f"Incorrect answer - {data['results'][0]['incorrect_answers']}")
if __name__ == "__main__":
    main()

