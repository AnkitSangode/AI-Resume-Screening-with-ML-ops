from resumeScreening.config.configuration import ConfigurationManager
from resumeScreening.components.deep_model_trainer import DeepModelTrainer
from src.resumeScreening import logger



class DeepModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            get_deep_model_trainer_config = config.get_deep_model_trainer_config()
            deep_model_training = DeepModelTrainer(get_deep_model_trainer_config)
            deep_model_training.train_and_save()
        except Exception as e:
            raise e
        
        
STAGE_NAME = "Deep Model Trainer"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> {STAGE_NAME} has started")
        obj = DeepModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> {STAGE_NAME} has completed successfully")
    except Exception as e:
        logger.exception(f"Error occurred in {STAGE_NAME}: {e}")
        raise e