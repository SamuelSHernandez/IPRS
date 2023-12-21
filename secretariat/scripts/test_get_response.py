import unittest
from unittest.mock import patch
import pandas as pd
from get_response import get_response

class TestGetResponse(unittest.TestCase):
    @patch('get_response.requests.get')
    def test_get_response_success(self, mock_get):
        # Mocked API response data
        mocked_data = [
            {
                "id": 1,
                "answers": [
                    {"question_id": 1, "answer": "Frequently"},
                    {"question_id": 2, "answer": "Occasionally"},
                ]
            },
            {
                "id": 2,
                "answers": [
                    {"question_id": 1, "answer": "Always"},
                    {"question_id": 2, "answer": "Never"},
                ]
            },
        ]

        # Mapping of answer labels
        LABEL_MAPPING = {
            "Never": 0,
            "Occasionally": 1,
            "Frequently": 2,
            "Always": 3,
        }

        # Simulate the processing of API response
        formatted_data = [
            {
                "id": entry["id"],
                "question_id": answer.get("question_id"),
                "answer": LABEL_MAPPING.get(answer.get("answer"), answer.get("answer")),
            }
            for entry in mocked_data
            for answer in entry.get("answers", [])
        ]
        # Create the expected DataFrame
        expected_dataframe = pd.DataFrame(formatted_data)
        # Drop specified columns
        columns_to_exclude = [
            "startTime", "submittedTime", "ip", "deviceType", "location",
            "browser", "browserLanguage", "os", "timeZone","totalScore",
        ]
        expected_dataframe = expected_dataframe.drop(columns=columns_to_exclude, errors="ignore")
        # Mock the requests.get method to return a response
        mock_get.return_value.json.return_value = {"data": mocked_data}

        result = get_response()
        self.assertIsNotNone(result)
        self.assertTrue(result.equals(expected_dataframe))

    @patch('get_response.requests.get')
    def test_get_response_failure(self, mock_get):
        # Mock the requests.get method to raise an exception
        mock_get.side_effect = Exception("Mocked error")

        result = get_response()
        self.assertIsNotNone(result)
        self.assertTrue(result.empty)

if __name__ == '__main__':
    unittest.main()
