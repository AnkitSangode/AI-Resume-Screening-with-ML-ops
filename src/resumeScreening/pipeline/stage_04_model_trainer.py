from resumeScreening.config.configuration import ConfigurationManager
from resumeScreening.components.model_trainer import ModelTrainer
from resumeScreening import logger

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            get_model_training_config = config.get_model_training_config()
            model_trainer = ModelTrainer(config = get_model_training_config)
            model_trainer.train_all()
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