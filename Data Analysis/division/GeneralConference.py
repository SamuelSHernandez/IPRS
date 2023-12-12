import csv
from abc import ABC, abstractmethod


class GeneralConference:
    _instance = None
    _id = "A11111"

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GeneralConference, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.divisions = []

    def add_division(self, division):
        self.divisions.append(division)

    def get_divisions(self):
        return self.divisions

    def get_id(self):
        return self._id



class AbstractInstitutionFactory(ABC):
    @abstractmethod
    def create_division(self, _id: str, name: str):
        pass

class DivisionFactory(AbstractInstitutionFactory):
    def create_division(self, _id: str, name: str):
        return Division(_id, name)

class Division:
    def __init__(self, _id: str, name: str):
        self._id = _id
        self.name = name

    def __str__(self):
        return f"{self.name}"


def read_divisions_from_csv(file_path):
    divisions = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            divisions.append(row)
    return divisions


# Assuming the CSV file has headers 'id' and 'name'
csv_file_path = "division.csv"

# Create the General Conference singleton instance
general_conference = GeneralConference()

# Create DivisionFactory instance
division_factory = DivisionFactory()

# Read divisions from CSV file
divisions_data = read_divisions_from_csv(csv_file_path)

# Create Division objects and add them to the General Conference instance
for division_data in divisions_data:
    div_instance = division_factory.create_division(_id=division_data['id'], name=division_data['name'])
    general_conference.add_division(div_instance)

# Print the list of divisions
for division in general_conference.get_divisions():
    print(f"{division._id}: {division}")
