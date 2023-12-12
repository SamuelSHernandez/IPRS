import csv
import json
from collections import defaultdict
import requests

def group_entries_by_union_id(entries):
    grouped_data = defaultdict(list)

    for entry in entries:
        union_id = entry.get("UnionID")
        grouped_data[union_id].append(entry)

    return grouped_data

def map_div_to_id():
    div_map = {
        0: ("East-Central Africa Division", "ECD"),
        1: ("Euroasia Division", "ESD"),
        2: ("Intereuropean Division", "EUD"),
        3: ("Interamerican Division", "IAD"),
        4: ("North American Division", "NAD"),
        5: ("Northern Asia Pacific Division", "NSD"),
        6: ("South American Division", "SAD"),
        7: ("South Pacific Division", "SPD"),
        8: ("Southern African Indian Ocean Division", "SID"),
        9: ("Southern Asia Division", "SUD"),
        10: ("Southern Asia Pacific Division", "SSD"),
        11: ("Transeuropean Division", "TED"),
        12: ("West Central Africa Division", "WAD"),
        13: ("Chinese Union Mission", "CHUM"),
        14: ("Middle East North African Union Mission", "MENAUM"),
    }
    return div_map

def fetch_data_from_api(api_url):
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error fetching data from API: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def export_to_csv(data, csv_file_path):
    div_map = map_div_to_id()

    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Name', 'UnionID', 'DivID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for union_id, entries in data.items():
            for entry in entries:
                div_id = entry.get('DivID', '')
                div_name, div_code = div_map.get(div_id, ("", ""))
                
                writer.writerow({
                    'ID': entry.get('EntityID', ''),
                    'Name': entry.get('Name', ''),
                    'UnionID': entry.get('UnionID', ''),
                    'DivID': div_code,
                })

def main(api_url, csv_file_path):
    try:
        data = fetch_data_from_api(api_url)

        if data:
            grouped_by_union_id = group_entries_by_union_id(data)
            export_to_csv(grouped_by_union_id, csv_file_path)
            print(f"CSV file '{csv_file_path}' created successfully.")
        else:
            print("No data fetched from the API.")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Replace 'your_api_endpoint' with the actual API endpoint
    api_url = "https://orgmast.adventist.org/OrgMastAPI/api/OMAdmfield?$filter=Active%20eq%20true"
    
    # Replace 'output.csv' with the desired CSV file path
    csv_file_path = "conference.csv"

    main(api_url, csv_file_path)
