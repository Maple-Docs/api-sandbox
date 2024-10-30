import requests
import json
import os
from dotenv import load_dotenv


if (__name__ == "__main__") :

    load_dotenv(dotenv_path = "../.env")

    headers = {
        "x-nxopen-api-key": os.getenv("API_KEY")
    }

    base_url = "https://open.api.nexon.com/maplestory/v1/id?"

    base_json = ".json"

    characterName = os.getenv("Character_Name")
    
    urlString = base_url + characterName
    # urlString = "https://open.api.nexon.com/maplestory/v1/character/list?" + characterName
    # urlString = "https://open.api.nexon.com/maplestory/v1/character/basic?ocid=" + ocid
    # urlString = "https://open.api.nexon.com/maplestory/v1/character/item-equipment?ocid=" + ocid

    response = requests.get(urlString, headers = headers)

    with open("out" + base_json, "w", encoding='utf-8') as f :
        json.dump(response.json(), f, ensure_ascii = False, indent = 4)
        
    # print(response)
    
    print("Done")
