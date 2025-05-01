# Rain Alert App

A Python application that sends email alerts when rain is forecasted in your area. Created as part of the ["100 Days of Python Bootcamp"](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu.

## Description

This application checks the weather forecast for your specified location using the OpenWeatherMap API. If rain is expected in the next few hours, it automatically sends you an email alert reminding you to take an umbrella.

## Features

* Fetches weather data from OpenWeatherMap API
* Detects rain in upcoming weather forecasts
* Sends automated email alerts
* Uses environment variables for secure credential storage

## Setup

1.  Clone this repository:
    ```bash
    git clone <repository_url> # Replace <repository_url> with the actual URL
    ```
2.  Navigate to the project directory:
    ```bash
    cd rain-alert-app # Or whatever your project directory is named
    ```
3.  Install required packages:
    ```bash
    pip install requests python-dotenv
    ```
4.  Create a file named `.env` in the project root directory with your email password:
    ```
    MY_EMAIL_PASS=your_password_here
    ```
    *Note: This file should not be committed to version control for security reasons. Consider adding `.env` to your `.gitignore` file.*
5.  Update the following variables in `main.py`:
    * `MY_LAT` and `MY_LONG` (your location coordinates)
    * `API_KEY` (your OpenWeatherMap API key)
    * `MY_EMAIL` (sender email)
    * `TO_EMAIL` (recipient email)

## Usage

Run the script with:

```bash
python main.py
```
## Acknowledgements

Project created as part of the ["100 Days of Python Bootcamp"](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu on Udemy.
