import logging
from app.app import answer
from app.utils import preprocess_input
from app.utils import is_us_zipcode
from app.exceptions import APIRequestError

SEPARATE_LINE = "--------------------------------"


def prompt_to_user(sentence: str):
    """
    Format string from input sentence to prompt to user
    """
    print('(^.^) ' + sentence)


def ask_yes_no(question: str) -> bool:
    """
    Ask user a yes/no question, return True if user says "yes"
    """
    prompt_to_user(question)
    return preprocess_input(input()) == "yes"


def main():
    """
    Main process
    """
    retry = True
    zip_code = None
    # zip_code = 30076
    # Ask for the zip code.
    # If valid, continue to next step
    # Else, ask for retry or exit
    while retry:
        prompt_to_user("Please tell me your US Zipcode [00601 - 99950]:")
        try:
            zip_code = int(input())
            if not is_us_zipcode(zip_code):
                raise ValueError()
            break
        except ValueError:
            prompt_to_user("Sorry your zip code is invalid.")
            print(SEPARATE_LINE)
            retry = ask_yes_no("Do you want to retry?")
    if zip_code is None:
        return

    # Ask for the question.
    # After answer, ask for retry or exit
    print(SEPARATE_LINE)
    retry = True
    while retry:
        prompt_to_user("May I help you?")
        question = input()
        if preprocess_input(question) == "no":
            return
        try:
            result = answer(zip_code, question)
            prompt_to_user(result)
            print(SEPARATE_LINE)
            retry = ask_yes_no("Do you want to ask anything else?")
        except APIRequestError:
            prompt_to_user("I'm sorry. Service is not available now. Please check the log file for more information.")
            break


if __name__ == '__main__':
    logging.basicConfig(
        filename='app/weather_app.log',
        filemode='w+',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s'
    )
    main()
    print(SEPARATE_LINE)
    prompt_to_user("Thank you! See you next time.")
