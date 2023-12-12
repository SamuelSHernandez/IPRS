from abc import ABC, abstractmethod

class AbstractInstitutionFactory(ABC):
    @abstractmethod
    def create_division(self, _id: str, name: str, countries: list):
        pass


class DivisionFactory(AbstractInstitutionFactory):
    def create_division(self, _id: str, name: str, countries: list):
        return Division(_id, name, countries)

class Division:
    def __init__(self, _id: str, name: str, countries: list):
        self._id = _id
        self.name = name
        self.countries = countries

    def __str__(self):
        return f"{self.name} Division"

    def get_countries(self)->list[str]:
        return self.countries

divisions_and_countries = {
    "North American Division (NAD)": ["United States", "Canada", "Bermuda", "Guam", "Micronesia", "Northern Mariana Islands", "Palau"],
    "South American Division (SAD)": ["Argentina", "Bolivia", "Brazil", "Chile", "Ecuador", "Paraguay", "Peru", "Uruguay"],
    "East-Central Africa Division (ECD)": ["Burundi", "Democratic Republic of the Congo", "Djibouti", "Eritrea", "Ethiopia", "Kenya", "Rwanda", "South Sudan", "Tanzania", "Uganda"],
    "Euro-Asia Division (ESD)": ["Armenia", "Azerbaijan", "Belarus", "Estonia", "Georgia", "Kazakhstan", "Kyrgyzstan", "Latvia", "Lithuania", "Moldova", "Russia", "Turkmenistan", "Ukraine", "Uzbekistan"],
    "Inter-American Division (IAD)": ["Anguilla", "Antigua and Barbuda", "Aruba", "Bahamas", "Barbados", "Belize", "Bermuda", "Bonaire", "British Virgin Islands", "Cayman Islands", "Colombia", "Costa Rica", "Cuba", "Curaçao", "Dominica", "Dominican Republic", "El Salvador", "French Guiana", "Grenada", "Guadeloupe", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Martinique", "Mexico", "Montserrat", "Nicaragua", "Panama", "Puerto Rico", "Saba", "Saint Barthelemy", "Saint Eustatius", "Saint Kitts and Nevis", "Saint Lucia", "Saint Martin", "Saint Pierre and Miquelon", "Saint Vincent and the Grenadines", "Sint Maarten", "Suriname", "Trinidad and Tobago", "Turks and Caicos Islands", "US Virgin Islands", "Venezuela"],
    "Inter-European Division (EUD)": ["Albania", "Andorra", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Gibraltar", "Greece", "Greenland", "Hungary", "Iceland", "Ireland", "Italy", "Kosovo", "Liechtenstein", "Luxembourg", "Malta", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "United Kingdom"],
    "Southern Africa-Indian Ocean Division (SID)": ["Angola", "Botswana", "Eswatini", "Lesotho", "Madagascar", "Malawi", "Mauritius", "Mozambique", "Namibia", "Réunion", "Seychelles", "South Africa", "Zambia", "Zimbabwe"],
    "Southern Asia Division (SUD)": ["Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives", "Nepal", "Pakistan", "Sri Lanka"],
    "South Pacific Division (SPD)": ["Australia", "New Zealand", "Papua New Guinea", "Solomon Islands", "Vanuatu", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "Palau", "Samoa", "Tonga", "Tuvalu"],
    "Trans-European Division (TED)": ["Albania", "Bosnia and Herzegovina", "Croatia", "Denmark", "Estonia", "Faroe Islands", "Finland", "Iceland", "Latvia", "Lithuania", "Norway", "Poland", "Sweden"],
    "West-Central Africa Division (WAD)": ["Benin", "Burkina Faso", "Cape Verde", "Côte d'Ivoire", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Liberia", "Mali", "Mauritania", "Niger", "Nigeria", "Senegal", "Sierra Leone", "Togo"],
    "Southern Asia-Pacific Division (SSD)": ["Brunei", "Cambodia", "East Timor", "Indonesia", "Laos", "Malaysia", "Myanmar", "Philippines", "Singapore", "Thailand", "Vietnam"],
    "General Conference of Seventh-day Adventists - Middle East and North Africa Union Mission (MENA)": ["Algeria", "Bahrain", "Egypt", "Iran", "Iraq", "Israel", "Jordan", "Kuwait", "Lebanon", "Libya", "Mauritania", "Morocco", "Oman", "Palestine", "Qatar", "Saudi Arabia", "Sudan", "Syria", "Tunisia", "United Arab Emirates", "Yemen"]
}

# Print the list of divisions and their countries
for division, countries in divisions_and_countries.items():
    print(f"{division} ({countries})")
