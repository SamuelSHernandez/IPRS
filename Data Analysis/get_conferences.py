import csv
import json
import requests
from collections import defaultdict
import logging as log
from DATA import api_url

CSV_FILE_PATH = "conference.csv"
FIELDNAMES = ['id', 'union_id', 'name']


def fetch_data_from_api(api_url):
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

def group_by_id(entries, id_key):
    """
    Groups entries by the specified ID key.

    Args:
        entries (list): List of entries to be grouped.
        id_key (str): Key to be used for grouping.

    Returns:
        defaultdict: Grouped data.
    """
    grouped_data = defaultdict(list)
    for entry in entries:
        identifier = entry.get(id_key)
        grouped_data[identifier].append(entry)
    log.debug(f"Grouped data by {id_key} successfully.")
    return grouped_data

def get_conferences(api_url, csv_file_path):
    """
    Main function to fetch data from the API, group it, and export to CSV.

    Args:
        api_url (str): URL of the API.
        csv_file_path (str): Path to the CSV file.
    """
    try:
        data = fetch_data_from_api(api_url)
        if data:
            union_id_group = group_by_id(data, "UnionID")
            export_to_csv(union_id_group, csv_file_path)
            log.info(f"CSV file '{csv_file_path}' created successfully.")
        else:
            log.info("No data fetched from the API.")
    except requests.RequestException as e:
        log.exception(f"Error fetching data from API: {e}")
    except json.JSONDecodeError as e:
        log.exception(f"Error decoding JSON: {e}")
    except Exception as e:
        log.exception(f"An unexpected error occurred: {e}")

def export_to_csv(data, csv_file_path):
    """
    Exports grouped data to a CSV file.

    Args:
        data (defaultdict): Grouped data.
        csv_file_path (str): Path to the CSV file.
    """
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writeheader()
        for _id, (identifier, entries) in enumerate(data.items()):
            for entry in entries:
                entry['ID'] = _id
                writer.writerow({
                    'id': entry.get('CustomID', ''),
                    'name': entry.get('Name', ''),
                    'union_id': entry.get('UnionID', ''),
                })


if __name__ == "__main__":
    log.basicConfig(level=log.INFO)
    get_conferences(api_url, CSV_FILE_PATH)
