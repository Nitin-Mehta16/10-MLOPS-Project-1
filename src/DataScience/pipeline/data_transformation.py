from src.DataScience.config.configuration  import ConfigurationManager
from src.DataScience.components.data_transformation import DataTransformation
from src.DataScience import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_DataTransformation(self):
        try:
            with open("artifact/data_validation/status.txt", 'r') as f:
                lines = f.readlines()
                has_error = any("False" in line for line in lines)
                status = not has_error
            if status==True:    
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("Your data scheme is not valid")
        except Exception as e:
            raise e