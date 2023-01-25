import requests
import re
import sys
domain = sys.argv[1]
# Wayback CDX API
url = f"http://web.archive.org/cdx/search/cdx?url={domain}/*&output=json&fl=original&collapse=urlkey"
response = requests.get(url)
wayback_urls = response.json()

# CommonCrawl
url = "https://index.commoncrawl.org/CC-MAIN-2022-22-index?url=*.{domain}/*&output=json"
response = requests.get(url)
commoncrawl_urls = response.json()



all_urls = wayback_urls + commoncrawl_urls

# Create an empty set to store recorded parameters
recorded_parameters = set()

for url in all_urls:
    parameters = re.findall(r'[?|&](\w+)=', url)
    for parameter in parameters:
        if parameter in recorded_parameters:
            print(parameter)
        else:
            recorded_parameters.add(parameter)
