import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path = "../.env")

headers = {
    "x-nxopen-api-key": os.getenv("API_KEY")
}

if (__name__ == "__main__") :

    characterName = os.getenv("Character_Name")
    
    urlString = "https://open.api.nexon.com/maplestory/v1/id?" + characterName
    # urlString = "https://open.api.nexon.com/maplestory/v1/character/list?" + characterName
    # urlString = "https://open.api.nexon.com/maplestory/v1/character/basic?ocid=" + ocid
    # urlString = "https://open.api.nexon.com/maplestory/v1/character/item-equipment?ocid=" + ocid

    response = requests.get(urlString, headers = headers)

    with open("out.json", "w", encoding='utf-8') as f :
        json.dump(response.json(), f, ensure_ascii = False, indent = 4)
        
    # print(response)
    
    print("Done")
