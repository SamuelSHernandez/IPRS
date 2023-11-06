#!/usr/bin/env python3

import sys
from acronym_list import general_conference_acronyms


def lookup_acronym(acronym: str, acronym_list: dict) -> str:
    for dictionary in acronym_list:
        if acronym in dictionary:
            return dictionary[acronym]

if len(sys.argv) < 2:
    print("Usage: python lookup_acronym.py [acronym]")
else:
    acronym = sys.argv[1]
    definition = lookup_acronym(acronym, general_conference_acronyms)
    print(f"{acronym}: {definition}")
