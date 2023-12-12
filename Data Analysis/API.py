import requests
import csv

def extract_hierarchy(data):
    hierarchy = []
    current_level = data["OrgLevel"]
    current_id = data["EntityID"]
    current_name = data["Name"]

    while current_level > 0:
        hierarchy.append({"ID": current_id, "Name": current_name})
        current_id = data["ParentEntityID"]
        
        # Fetch the parent data to get the correct name for the parent level
        parent_data = get_parent_data(current_id)  # Implement this function
        current_name = parent_data.get("Name") if parent_data else None
        
        current_level -= 1

    return reversed(hierarchy)


def get_parent_data(entity_id):
    # Implement logic to fetch data for the given entity ID from your API
    # Make a request to the API to get data for the specified entity ID
    parent_url = f"https://orgmast.adventist.org/OrgMastAPI/api/OMAdmfield/{entity_id}"
    parent_response = requests.get(parent_url)

    if parent_response.status_code == 200:
        return parent_response.json()
    else:
        print(f"Error fetching parent data: {parent_response.status_code} - {parent_response.text}")
        return None


def export_to_csv(hierarchy):
    with open('hierarchy.csv', 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for level in hierarchy:
            writer.writerow(level)

url = "https://orgmast.adventist.org/OrgMastAPI/api/OMAdmfield?$filter=Active%20eq%20true"

# Make the API call
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Assuming the response is a list of records
    for record in data:
        # Access and print relevant fields (adjust based on the actual structure of the response)
        print("Field ID:", record.get("FieldID"))
        print("Field Name:", record.get("FieldName"))
        print("Active:", record.get("Active"))

        # Extract hierarchy and export to CSV
        hierarchy = extract_hierarchy(record)
        export_to_csv(hierarchy)
        print("-------------")

else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code} - {response.text}")
