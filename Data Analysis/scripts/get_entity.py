import csv
import logging as log
from collections import defaultdict

import requests
from DATA import api_url, union_dict

CSV_FILE_PATH = "Data/conference.csv"
CONFERENCE_FIELDNAMES = ["id", "union_id", "name"]


class ApiFetcher:
    """
    A class for fetching data from an API.
    """

    @staticmethod
    def fetch_data(api_url):
        """
        Fetches data from the specified API URL.

        Args:
            api_url (str): URL of the API.

        Returns:
            dict: Fetched JSON data.
        """
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            log.error(f"Error fetching data from API: {e}")
            return None


class CsvExporter:
    """
    A class for exporting data to a CSV file.
    """

    @staticmethod
    def export_to_csv(data, file_path):
        """
        Exports grouped data to a CSV file.

        Args:
            data (defaultdict): Grouped data.
            file_path (str): Path to the CSV file.
        """
        with open(file_path, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=CONFERENCE_FIELDNAMES)
            writer.writeheader()
            id_counter = 0
            for parent_id, child_entries in data.items():
                for _, child_entry in enumerate(child_entries):
                    writer.writerow(
                        {
                            "id": id_counter,
                            "name": child_entry.get("Name", ""),
                            "union_id": parent_id,
                        }
                    )
                    id_counter += 1


class DataManager:
    """
    A base class for managing data.
    """

    def __init__(self, api_fetcher, csv_exporter):
        self.api_fetcher = api_fetcher
        self.csv_exporter = csv_exporter

    def get_data(self, api_url):
        """
        Abstract method to fetch data.

        Args:
            api_url (str): URL of the API.

        Returns:
            dict: Fetched data.
        """
        raise NotImplementedError("Subclasses must implement get_data method")

    def process_data(self, data, file_path):
        """
        Abstract method to process and export data.

        Args:
            data: Data to process.
            file_path (str): Path to the CSV file.
        """
        raise NotImplementedError("Subclasses must implement process_data method")


class ConferenceDataManager(DataManager):
    """
    A class for managing conference data.
    """

    def get_data(self, api_url):
        data = self.api_fetcher.fetch_data(api_url)
        if data:
            conference_dict = defaultdict(list)
            for _child in data:
                parent_code = _child.get("ParentID")
                if any(parent_code == code for _, code in union_dict.values()):
                    parent_id = next(
                        key
                        for key, (_, code) in union_dict.items()
                        if code == parent_code
                    )
                    conference_dict[parent_id].append(_child)
            return conference_dict
        return None

    def process_data(self, data, file_path):
        self.csv_exporter.export_to_csv(data, file_path)
        log.info(f"CSV file '{file_path}' created successfully.")


def main():
    """
    Main function to demonstrate the use of ConferenceDataManager.
    """
    log.basicConfig(level=log.INFO)
    conference_manager = ConferenceDataManager(ApiFetcher(), CsvExporter())
    conference_data = conference_manager.get_data(api_url)
    conference_manager.process_data(conference_data, CSV_FILE_PATH)


if __name__ == "__main__":
    main()
