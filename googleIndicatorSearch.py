#!/usr/bin/python3
"""
Programmatically find relationships between a list of strings using Google.

Usage: python3 googleIndicatorSearch.py
"""

import googlesearch
from termcolor import colored
import yaml


yaml_list = """

static_strings:
    # - "index of /"        # Example

list_to_check_against:
    # - "16Shop-Apple-V1."  # Example

"""

def return_results():
    """Return results from Google."""
    loaded = yaml.safe_load(yaml_list)
    static_strings = loaded["static_strings"]
    list_to_check_against = loaded["list_to_check_against"]

    if len(static_strings) == 0 or len(list_to_check_against) == 0:
        exit()

    for static_string in static_strings:
        for ltca_string in list_to_check_against:
            if static_string == ltca_string:
                continue

            query = '"{}" "{}"'.format(static_string, ltca_string)
            resp = googlesearch.search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0, user_agent="Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko")
            results = "\n".join(resp)

            print(colored("{} --> {}".format(static_string, ltca_string), "green"))
            print(results)
            print("")
    return

return_results()
