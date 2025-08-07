from resumeScreening.config.configuration import ConfigurationManager
from resumeScreening.components.model_evaluation import ModelEvaluation
from resumeScreening import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_eval_config = config.get_model_evaluation_config()
            evaluator = ModelEvaluation(config=model_eval_config)
            evaluator.evaluate()
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