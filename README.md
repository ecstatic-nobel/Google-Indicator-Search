# [Google Indicator Search]  
##### Programmatically find the relationship of a list of strings using Google.  

### Use Cases  
- Detect signs of potential threats in public places  
    - Add list of public place to `static_strings`  
    - Add list of trigger/angry words/phrases to `list_to_check_against`  
    - Run `python3 googleIndicatorSearch.py` to find possible relationships  

- Detected defaced websites along with threat actor names  
    - Add name of the threat actor to `static_strings`  
    - Add list of keywords to `list_to_check_against`  
    - Run `python3 googleIndicatorSearch.py` to find possible relationships  

- Detected publicly accessible webshells  
    - Add name of the webshell to `static_strings`  
    - Add list of keywords to `list_to_check_against`  
    - Run `python3 googleIndicatorSearch.py` to find possible relationships  

### Prerequisities  
- Ubuntu 18.04 (should work on other Linux distros)  
- Python 3.7.3  
- Python 3 Pip  
- DEB Packages:  
  - gcc  

### Setup  
Run the following command to install Pip packages:  
```bash
pip3 install -r requirements.txt  
```

### Usage  
- Add static strings to the `static_string` list  
- Add all other strings to the `list_to_check_against` list  
- Run:
```bash
python3 googleIndicatorSearch.py  
```

### Things to know  
- Be responsible!!!  
- This program is only as strong as the yaml lists  
- Using a Python virtual environment is highly recommended  
- Too many requests will result in a `urllib.error.HTTPError: HTTP Error 429: Too Many Requests` error  

Please fork, create merge requests, and help make this better.  
