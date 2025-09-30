## 📁 components/ → 🧩 Reusable building blocks (e.g., data ingestion, preprocessing, training, evaluation). Each  script handles one major step.

from src.DataScience.config.configuration  import ConfigurationManager
from src.DataScience.components.data_validation import DataValiadtion
from src.DataScience import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_dataValidation(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_validation_config()
        data_ingestion=DataValiadtion(config=data_ingestion_config)
        data_ingestion.validate_all_columns()
        data_ingestion.validate_columns_type()