import pandas as pd

class DataPreprocessor:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir

    def preprocess_csv(self, file_name: str):
        file_path = f"{self.data_dir}/{file_name}"
        df = pd.read_csv(file_path)

        df.dropna(thresh=int(0.9 * len(df.columns)), inplace=True)
        
        # Rename columns to lowercase for consistency
        df.columns = [col.lower() for col in df.columns]
        
        # Droping unnecessary columns from socioeconomic data
        if file_name == "socioeconomic_data.csv":
            columns_to_drop = [
                # Geospatial and metadata
                'shape__area', 'shape__length', 'geoid', 'stusab', 'name',
                
                # Detailed income data
                'b19001_lt15', 'b19001_15to25', 'b19001_25to35', 'b19001_35to45', 'b19001_45to60', 'b19001_gt150',
                'b19001_lt15_pct', 'b19001_15to25_pct', 'b19001_25to35_pct', 'b19001_35to45_pct', 'b19001_45to60_pct', 'b19001_gt150_pct',
                
                # Detailed employment data by age
                'b23001_clf', 'b23001_ue', 'b23001_ue_pct', 'b23001_16to24', 'b23001_ue_16to24', 'b23001_ue_16to24_pct', 'b23001_25to64', 
                'b23001_ue_25to64', 'b23001_ue_25to64_pct', 'b23001_above64', 'b23001_ue_above64', 'b23001_ue_above64_pct',
                
                # Travel time breakdowns
                'b08013est1', 'b08303est1', 'b08303_30minus_ttw', 'b08303_30to59_ttw', 'b08303_60plus_ttw',
                'b08303_30minus_ttw_pct', 'b08303_30to59_ttw_pct', 'b08303_60plus_ttw_pct',
                
                # Room crowding details
                'b25014_crowd', 'b25014_crowd_pct', 'b25014_noncrowd_o', 'b25014_modcrowd_o', 'b25014_sevcrowd_o',
                'b25014_noncrowd_r', 'b25014_modcrowd_r', 'b25014_sevcrowd_r',
                'b25014_noncrowd_o_pct', 'b25014_modcrowd_o_pct', 'b25014_sevcrowd_o_pct',
                'b25014_noncrowd_r_pct', 'b25014_modcrowd_r_pct', 'b25014_sevcrowd_r_pct',
                
                # Housing cost details
                'b25106_cb_lt35', 'b25106_cb_gt35', 'b25106_cb_o_lt35', 'b25106_cb_o_gt35', 
                'b25106_cb_r_lt35', 'b25106_cb_r_gt35',
                'b25106_cb_lt35_pct', 'b25106_cb_gt35_pct', 'b25106_cb_o_lt35_pct', 'b25106_cb_o_gt35_pct',
                'b25106_cb_r_lt35_pct', 'b25106_cb_r_gt35_pct',
                
                # Occupational details
                'c24010_cemr', 'c24010_ptm', 'c24010_cemr_pct', 'c24010_ptm_pct',
                
                # Education and employment status details
                'b23006est6', 'b23006est6_pct', 'b23006est7', 'b23006est7_pct', 'b23006est8', 'b23006est8_pct',
                'b23006est13', 'b23006est13_pct', 'b23006est14', 'b23006est14_pct', 'b23006est15', 'b23006est15_pct',
                'b23006est20', 'b23006est20_pct', 'b23006est21', 'b23006est21_pct', 'b23006est22', 'b23006est22_pct',
                'b23006est27', 'b23006est27_pct', 'b23006est28', 'b23006est28_pct', 'b23006est29', 'b23006est29_pct'
            ]
            df.drop(columns=columns_to_drop, errors='ignore', inplace=True)
        
        # Save cleaned file
        df.to_csv(file_path, index=False)
        print(f"Preprocessed data saved to {file_path}")

    def preprocess_all(self):
        for file_name in ["windmill_data.csv", "socioeconomic_data.csv"]:
            self.preprocess_csv(file_name)
