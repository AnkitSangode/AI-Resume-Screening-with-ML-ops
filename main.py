from src.resumeScreening import logger
from src.resumeScreening.pipeline.stage_01_data_ingestion import DataIngestionPipeline



STAGE_NAME = "Data Ingestion"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> {STAGE_NAME} completed successfully <<<<<<<<<<<")
    except Exception as e:
        raise e