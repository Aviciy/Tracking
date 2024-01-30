import json
import requests

from Config import api_key, url

def track_package(tracking_number, carrier_code):
    headers = {
        "Content-Type": "application/json",
        "Trackingmore-Api-Key": api_key
    }
    data = {
        "tracking_number": tracking_number,
        "carrier_code": carrier_code
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.json())
    else:
        return response.json()

def save_tracking_info_to_file(tracking_info, file_name):
    with open(file_name, 'w') as file:
        json.dump(tracking_info, file, indent=4)

tracking_number = "SK479333958LV"
carrier_code = "cainiao"

tracking_info = track_package(tracking_number, carrier_code)
print(tracking_info)

# Збереження результатів у файл
save_tracking_info_to_file(tracking_info, 'tracking_info.json')
