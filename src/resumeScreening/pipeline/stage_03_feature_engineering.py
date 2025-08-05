from resumeScreening.config.configuration import ConfigurationManager
from resumeScreening.components.feature_engineering import FeatureEngineering
from resumeScreening import logger



STAGE_NAME = 'Feature Engineering'

class FeatureEngineeringPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            get_feature_engineering_config = config.get_feature_engineering_config()
            feature_engineering = FeatureEngineering(config= get_feature_engineering_config)
            feature_engineering.run()
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<")
        obj = FeatureEngineeringPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> {STAGE_NAME} completed successfully <<<<<<<<<<<")
    except Exception as e:
        raise e