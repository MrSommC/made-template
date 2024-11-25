import os
import pandas as pd
from sqlalchemy import create_engine
from downloader import DataRetriever
from preprocessor import DataPreprocessor

class DataPipeline:
    def __init__(self, db_name: str):
        self.data_dir = "/Users/christophsommermann/Documents/made-template/data"
        self.db_path = os.path.join(self.data_dir, db_name + ".sqlite")
        self.engine = create_engine(f"sqlite:///{self.db_path}", echo=False)

    def download_data(self):
        data_retriever = DataRetriever(self.data_dir)
        datasets = {
            "windmill_data": "https://www.sciencebase.gov/catalog/file/get/6001e327d34e592d8671fae0?name=uswtdb_v7_1_20240814.csv",
            "socioeconomic_data": "https://services.arcgis.com/VTyQ9soqVukalItT/arcgis/rest/services/ACS_5YR_Socioeconomic_Estimate_Data_by_State/FeatureServer/17/query?where=1%3D1&outFields=*&outSR=4326&f=json"
        }

        data_retriever.download_csv(datasets["windmill_data"], "windmill_data.csv")
        data_retriever.download_api_data(datasets["socioeconomic_data"], "socioeconomic_data.csv")

    def preprocess_data(self):
        preprocessor = DataPreprocessor(self.data_dir)
        preprocessor.preprocess_all()


    def save_data(self):
        print("Saving data to SQLite database...")
        with self.engine.connect() as conn:
            for file_name in ["windmill_data.csv", "socioeconomic_data.csv"]:
                df = pd.read_csv(os.path.join(self.data_dir, file_name))
                table_name = file_name.split(".")[0]
                df.to_sql(table_name, conn, if_exists='replace', index=False)
        print("Data saved successfully.")
        self.engine.dispose()

    def run_pipeline(self):
        self.download_data()
        self.preprocess_data()
        self.save_data()

if __name__ == "__main__":
    pipeline = DataPipeline("renewable_energy_data")
    pipeline.run_pipeline()
