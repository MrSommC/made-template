import unittest
import os
import sqlite3

from pipeline import DataPipeline

class TestDataPipelineSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_dir = "/Users/christophsommermann/Documents/made-template/data"
        cls.db_name = "test_renewable_energy_data"
        cls.db_path = os.path.join(cls.data_dir, cls.db_name + ".sqlite")
        cls.pipeline = DataPipeline(db_name=cls.db_name)

        # Clean up before testing
        if os.path.exists(cls.db_path):
            os.remove(cls.db_path)

    def test_pipeline_end_to_end(self):
        # Run the pipeline
        self.pipeline.run_pipeline()

        # Check if the database was created
        self.assertTrue(os.path.exists(self.db_path), "Database was not created.")

        # Check if required tables exist
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [table[0] for table in cursor.fetchall()]

        self.assertIn("windmill_data", tables, "Table 'windmill_data' is missing.")
        self.assertIn("socioeconomic_data", tables, "Table 'socioeconomic_data' is missing.")

if __name__ == "__main__":
    unittest.main()
