import pandas as pd
import requests
import logging

# Configuration
SURVEY_ID = "453729"
LIMIT = "10"
API_TOKEN = "prfLeeUjVxqA6Jpj21YEMBc8euvJ8vUUqClXwmEyzL5vlSBMCgeMXxn2hMh7A2-cgcXrwOXUcW32P5rwizUaeiGg"
URL = f"https://api.surveysparrow.com/v3/responses?survey_id={SURVEY_ID}&limit={LIMIT}"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

LABEL_MAPPING = {
    "Never": 0,
    "Occasionally": 1,
    "Frequently": 2,
    "Always": 3,
}

try:
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()
    # Extract relevant data
    data = response.json()["data"]
    formatted_data = [
        {
            "id": entry["id"],
            "question_id": answer.get("question_id"),
            "answer": LABEL_MAPPING.get(answer.get("answer"), answer.get("answer")),
        }
        for entry in data
        for answer in entry.get("answers", [])
    ]
    survey_data = pd.DataFrame(formatted_data)
    columns_to_exclude = [
        "startTime", "submittedTime", "ip", "deviceType", "location",
        "browser", "browserLanguage", "os", "timeZone"
    ]
    # This is the pandas dataframe being used by PowerBI
    survey_data = survey_data.drop(columns=columns_to_exclude, errors="ignore")

except requests.exceptions.RequestException as e:
    logging.error(f"An error occurred during the request: {str(e)}")
except Exception as e:
    logging.error(f"An unexpected error occurred: {str(e)}")
