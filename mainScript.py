import requests
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('API_TOKEN')
activites_url = "https://www.strava.com/api/v3/athlete/activities"

page = 1

while True:
    header = {'Authorization': 'Bearer ' + token}
    param = {'per_page': 200, 'page': page}
    response = requests.get(activites_url, headers=header, params=param)

    if response.status_code == 200:

        data = response.json()

        if len(data) == 0:
            print("--------------No more data-----------")
            print(response.json())
            print("--------------Last page-----------")
            print(page)
            break
        # do something with the data
        timestamp = time.time()
        with open("jsons/" + str(timestamp) + "-data.json", "w") as file:
            json.dump(data, file)
        print("Page downloaded: " + str(page))    
        page += 1
    elif response.status_code == 429:
        print("--------------Waiting for more available requests-----------")
        page += 1
        time.sleep(900)
    else:
        # handle the error
        print("--------------ERROR-----------")
        print(response.json())
        print("--------------Last page-----------")
        print(page)
        break