## 📁 config/ -> ⚙️Python helpers to load/parse config.yaml and schema.yaml.

from src.DataScience.entity.config_entity import DataIngestion_config, DataValidation_config,DataTransformationConfig, ModelTrainerConfig ,ModelEvaluationConfig
from src.DataScience.constants import *
from src.DataScience.utils.common import read_yaml, create_directories

from dotenv import load_dotenv
load_dotenv()
import os
MLFLOW_TRACKING_URI=os.getenv("MLFLOW_TRACKING_URI")
MLFLOW_TRACKING_USERNAME=os.getenv("MLFLOW_TRACKING_USERNAME")
MLFLOW_TRACKING_PASSWORD=os.getenv("MLFLOW_TRACKING_PASSWORD")
class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH,
                schema_filepath = SCHEMA_FILE_PATH):

        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        self.schema=read_yaml(schema_filepath)

        create_directories([self.config.artifact_dir])

    
    def get_data_ingestion_config(self) -> DataIngestion_config :
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestion_config(
            root_dir=config.root_dir,
            url=config.url,
            input_dir=config.input_dir,
            output_dir=config.output_dir
        )  
        return data_ingestion_config
    

##📁 config/ -> ⚙️Python helpers to load/parse config.yaml and schema.yaml.
    def get_data_validation_config(self) -> DataValidation_config :
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidation_config(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config
    



    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name
            
        )

        return model_trainer_config
    

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config=self.config.model_evaluation
        params=self.params.ElasticNet
        schema=self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config=ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path = config.model_path,
            all_params=params,
            metric_file_name = config.metric_file_name,
            target_column = schema.name,
            mlflow_uri= MLFLOW_TRACKING_URI
        )
        return model_evaluation_config