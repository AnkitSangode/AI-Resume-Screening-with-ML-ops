
from resumeScreening import logger
from resumeScreening.utils.common import clean_resume
from sklearn.model_selection import train_test_split
import pandas as pd
from resumeScreening.config.configuration import DataTransformationConfig
from pathlib import Path


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def data_transformation(self):
        df = pd.read_csv(self.config.data_path)

        df["Cleaned_Resume"] = df["Resume"].apply(clean_resume)

        # Save full cleaned data
        cleaned_path = Path(self.config.root_dir)/"cleaned_data.csv"
        df.to_csv(cleaned_path, index=False)

        # Train-test split
        train, test = train_test_split(df, test_size=0.2, random_state=42)

        # Save splits
        train.to_csv(Path(self.config.root_dir)/"train.csv", index=False)
        test.to_csv(Path(self.config.root_dir)/"test.csv", index=False)

        logger.info(f"[✓] Data cleaned and split. Files saved at: {self.config.root_dir}")
        