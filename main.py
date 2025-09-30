from src.DataScience import logger
from src.DataScience.pipeline.data_ingestion import DataingestionTrainingPipeline
from src.DataScience.pipeline.data_validation import DataValidationTrainingPipeline
from src.DataScience.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.DataScience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline


logger.info("Welcome to MLOPS-PROJECT-1 \n")


STAGE_NAME = "Data Ingestion Stage"
try:
        logger.info(f"-----------------------{STAGE_NAME} Started -------------------------------\n")
        obj = DataingestionTrainingPipeline()
        obj.initiate_dataingestion()
        logger.info(f"-----------------------{STAGE_NAME} Completed ------------------------------\n")

except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation Stage"
try:
        logger.info(f"-----------------------{STAGE_NAME} Started -------------------------------\n")
        obj = DataValidationTrainingPipeline()
        obj.initiate_dataValidation()
        logger.info(f"-----------------------{STAGE_NAME} Completed ------------------------------\n")

except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transformation Stage"
try:
        logger.info(f"-----------------------{STAGE_NAME} Started -------------------------------\n")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_DataTransformation()
        logger.info(f"-----------------------{STAGE_NAME} Completed ------------------------------\n")

except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.initiate_model_training()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e