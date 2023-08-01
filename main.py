import requests
from datetime import datetime
import os


APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
AUTHORIZATION = os.environ["AUTHORIZATION"]
sheety_workouts_url = "https://api.sheety.co/0db3b736d8cdef7d85e25973d8c7ae2c/myWorkouts/list1"
DATE = datetime.now().strftime("%d/%m/%Y")
TIME = datetime.now().strftime("%H:%M:%S")
# print(os.environ["APP_ID"])
HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Authorization": AUTHORIZATION
}

exercise_endpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("What exercises you did?")

GENDER = "male"
WEIGHT_KG = 75
HEIGHT = 180.5
AGE = 30
parameters_exercise = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE
}

exercise_request = requests.post(url=exercise_endpoints, json=parameters_exercise, headers=HEADER)
exercise_request.raise_for_status()
response = exercise_request.json()
# print(response)

EXERCISE = response['exercises'][0]['name'].title()
DURATION = response['exercises'][0]['duration_min']
CALORIES = response['exercises'][0]['nf_calories']
# print(EXERCISE)
# print(type(DURATION))
# print(CALORIES)

sheety_params = {
    "list1": {
    "date": DATE,
    "time": TIME,
    "exercise": EXERCISE,
    "duration": f"{DURATION}min",
    "calories": CALORIES
}
}

insert_into_sheet = requests.post(url=sheety_workouts_url, json=sheety_params)
insert_into_sheet.raise_for_status()