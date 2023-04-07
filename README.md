# weather-test

![Alt Text](/doc/demo.gif)

## Environment Preparation

### Required installations

- Python 3
- Configure python3 as the default command for "python"

### Setup project

- From command line go to project root directory
- Run the command:

```
pip install -r requirements.txt
```

## Run the program

- From command line go to project root directory
- Run the command:

```
python main.py
```

- Answer the question for your zipcode.
- Ask the program following questions:
  - Should I go outside?
  - Should I wear sunscreen?
  - Can I fly my kite?
- The program will answer:
  - "YES" or "NO" for your question which it knows.
  - "I don't know" if the question is not in the list above.

### Notes:

- US zip code will be validated in range from 00501 to 99950.
- The question can be case-insensitive and special characters will be ignored. For example these questions will be accepted:
  - "should I go Outside???"
  - "Should I go outside"
  - "can i fly my kite."
- Weather information will be logged in weather_app.log file inside "app" directory.

## Run the tests

- From command line go to project root directory
- Run the command:

```
python -m unittest discover
```

- All the test cases in tests directory of the project will be run.

## Project structure

- app: Main source directory
  - api.py: Module to request Weather Stack API
  - app.py: Main module to answer the question from user
  - config.py: Module to define dynamic configuration
  - exceptions.py: Module to define app handled exceptions
  - models.py: Module to define data models
  - service.py: Module to provide the decision for questions from the weather information
  - utils.py: Module to define utility functions
  - weather_app.log: Logging file is writen after running the program
- tests: Unittest source directory
  - test_api.py: Testcases for app.api module
  - test_models.py: Testcases for app.models module
  - test_services.py: Testcases for app.services module
  - test_utils.py: Testcases for app.utils module

### Notes:

- Test cases names are meaningful to describe which result if conditions matched