from resumeScreening.config.configuration import ConfigurationManager
from resumeScreening.components.data_ingestion import DataIngestion
from resumeScreening import logger

STAGE_NAME = "Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingeston_config = config.get_data_ingestion()
            data_ingestion = DataIngestion(config = data_ingeston_config)
            data_ingestion.download_data()
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> {STAGE_NAME} completed successfully <<<<<<<<<<<")
    except Exception as e:
        raise e