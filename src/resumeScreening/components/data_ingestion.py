from resumeScreening import logger
import pandas as pd
import os
from resumeScreening.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        os.makedirs('artifacts/data_ingestion',exist_ok=True)
        data = pd.read_csv(self.config.source_url)
        
        data.to_csv(self.config.local_data_file, index=False)

        logger.info(f"✅ Data downloaded and saved to: {self.config.local_data_file}")