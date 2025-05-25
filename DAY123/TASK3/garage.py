import requests
from dotenv import load_dotenv
import os
import json as json
import json_data_parser as JSONparsing
import fileLogs
import infoLogs
from car import Car                     

class garage:
    def __init__(self):
        load_dotenv()
        self.api = os.getenv('API_TOKEN')
        self.folder_path = r'C:\Users\trilo\Desktop\python_core_task\DAY123\TASK3\yourCars'  

    def addNewCar(self, make, year, model):
        infoLogs.logInfo("user call utility : addNewCar")
        api_url = f'https://api.api-ninjas.com/v1/cars?make={make}&model={model}&year={year}'  
        response = requests.get(api_url, headers={'X-Api-Key': self.api})
        if response.status_code == requests.codes.ok:
            parsed_data = JSONparsing.parser(response)
            if parsed_data:
                yourCar = Car(make, year, model, parsed_data)  
            else:
                fileLogs.logError("Error parsing JSON data")
                return
        else:
            fileLogs.logError(f"Error: {response.status_code} {response.text}")
            return

        os.makedirs(self.folder_path, exist_ok=True)          
        file_path = os.path.join(self.folder_path, f'{model}.json')
        with open(file_path, 'w') as file:
            file.write(json.dumps(yourCar.to_dict(), indent=4))
            print(f"{model}.json saved")

    def remove_car(self, car_name):
        infoLogs.logInfo("user call utility : remove_car")
        target = os.path.join(self.folder_path, f'{car_name}.json')
        if os.path.exists(target):
            os.remove(target)
            print(f"{car_name}.json has been removed from yourCars")
        else:
            print("Car not found")

    def list_out_cars(self):
        infoLogs.logInfo("user call utility : list_out_cars")
        if not os.path.exists(self.folder_path):
            print("No cars found in yourCars")
            return
        files = os.listdir(self.folder_path)
        if files:
            print("Your cars are:")
            for file in files:
                print(file)
        else:
            print("No cars found in yourCars")
