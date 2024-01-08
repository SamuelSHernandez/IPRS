import pandas as pd
import requests
import logging

def get_response():
    # Configuration
    SURVEY_ID = "453729"    # SEC - Functions & Facilities
    URL = f"https://api.surveysparrow.com/v3/responses?survey_id={SURVEY_ID}"
    API_TOKEN = "prfLeeUjVxqA6Jpj21YEMBc8euvJ8vUUqClXwmEyzL5vlSBMCgeMXxn2hMh7A2-cgcXrwOXUcW32P5rwizUaeiGg"
    HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}
    LABEL_MAPPING = {
        "Never": 0,
        "Occasionally": 1,
        "Frequently": 2,
        "Always": 3,
    }

    try:
        # Make the request
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

        # Create a Pandas DataFrame
        df = pd.DataFrame(formatted_data)

        # Drop specified columns
        columns_to_exclude = [
            "startTime", "submittedTime", "ip", "deviceType", "location",
            "browser", "browserLanguage", "os", "timeZone","totalScore",
        ]
        df = df.drop(columns=columns_to_exclude, errors="ignore")

        return df

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred during the request: {str(e)}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return pd.DataFrame()  # Return an empty DataFrame in case of unexpected error
    
survey_data = get_response()

# Check if the DataFrame is not empty before exporting to CSV
if not survey_data.empty:
    # Define the path where you want to save the CSV file
    csv_file_path = "data_analysis/survey_responses.csv"
    
    # Export the DataFrame to CSV
    survey_data.to_csv(csv_file_path, index=False)
    print(f"Survey responses exported to {csv_file_path}")
else:
    print("No survey responses to export.")