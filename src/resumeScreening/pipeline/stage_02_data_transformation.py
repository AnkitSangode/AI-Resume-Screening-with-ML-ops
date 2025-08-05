from resumeScreening.config.configuration import ConfigurationManager
from resumeScreening.components.data_transformation import DataTransformation
from resumeScreening import logger

STAGE_NAME = "Data Transformation"
class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config= data_transformation_config)
            data_transformation.data_transformation()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> {STAGE_NAME} completed successfully <<<<<<<<<<<")
    except Exception as e:
        raise e

