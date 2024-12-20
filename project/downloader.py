import os
import requests
import pandas as pd

class DataRetriever:
    def __init__(self, data_dir: str) -> None:
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)

    def download_csv(self, url: str, file_name: str) -> None:
        
        #Downloads a CSV file from the given URL or creates a mock file if mocking is enabled.
        
        file_path = os.path.join(self.data_dir, file_name)
        
        # Check if mocking is enabled
        if os.getenv("MOCK_DOWNLOAD", "false").lower() == "true":
            print(f"Mocking CSV download for {file_name}")
            # Create a mock CSV file
            mock_data = {"column1": [1, 2, 3], "column2": ["a", "b", "c"]}
            pd.DataFrame(mock_data).to_csv(file_path, index=False)
            print(f"Mock CSV file '{file_name}' created at {file_path}")
        else:
            # Download the file if it doesn't exist
            if not os.path.exists(file_path):
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                print(f"CSV file '{file_name}' downloaded from {url} and saved to {file_path}")

    def download_api_data(self, url: str, file_name: str) -> None:
        """
        Fetches data from an API or creates mock API data if mocking is enabled.
        """
        file_path = os.path.join(self.data_dir, file_name)
        
        # Check if mocking is enabled
        if os.getenv("MOCK_DOWNLOAD", "false").lower() == "true":
            print(f"Mocking API data download for {file_name}")
            # Create a mock API data file
            mock_data = {"mock_key": "mock_value"}
            pd.DataFrame([mock_data]).to_csv(file_path, index=False)
            print(f"Mock API data file '{file_name}' created at {file_path}")
        else:
            # Fetch data from API
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            json_data = response.json()
            
            attributes_data = [feature['attributes'] for feature in json_data['features']]
            
            df = pd.DataFrame(attributes_data)
            df.to_csv(file_path, index=False)
            print(f"API data from {url} fetched and saved as '{file_name}' at {file_path}")
