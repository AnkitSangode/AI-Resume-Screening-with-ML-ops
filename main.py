from src.resumeScreening import logger
from src.resumeScreening.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.resumeScreening.pipeline.stage_02_data_transformation import DataTransformationPipeline
from src.resumeScreening.pipeline.stage_03_feature_engineering import FeatureEngineeringPipeline
from src.resumeScreening.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from src.resumeScreening.pipeline.stage_05_deep_model_trainer import DeepModelTrainerPipeline
from src.resumeScreening.pipeline.stage_06_model_evaluation import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> {STAGE_NAME} completed successfully <<<<<<<<<<<")
    except Exception as e:
        raise e
    

STAGE_NAME = "Data Transformation"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> {STAGE_NAME} completed successfully <<<<<<<<<<<")
    except Exception as e:
        raise e
    

STAGE_NAME = 'Feature Engineering'

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<")
        obj = FeatureEngineeringPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> {STAGE_NAME} completed successfully <<<<<<<<<<<")
    except Exception as e:
        raise e


STAGE_NAME = 'Model Trainer'

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> {STAGE_NAME} completed successfully <<<<<<<<<<<")
    except Exception as e:
        raise e
    

STAGE_NAME = "Deep Model Trainer"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<")
        obj = DeepModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> {STAGE_NAME} completed successfully <<<<<<<<<<<")
    except Exception as e:
        raise e


STAGE_NAME = "Model Evaluation"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> {STAGE_NAME} has started")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> {STAGE_NAME} has completed successfully")
    except Exception as e:
        logger.exception(f"Error occurred in {STAGE_NAME}: {e}")
        raise e