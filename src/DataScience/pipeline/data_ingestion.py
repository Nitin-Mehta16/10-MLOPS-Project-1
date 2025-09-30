## 📁 pipeline/ → 🔗 Orchestration scripts that connect components (end-to-end ML pipeline).


from src.DataScience.config.configuration  import ConfigurationManager
from src.DataScience.components.data_ingestion import DataIngestion
from src.DataScience import logger

STAGE_NAME = "Data Ingestion Stage"

class DataingestionTrainingPipeline:
    def _init_(self):
        pass

    def initiate_dataingestion(self):
        config= ConfigurationManager()
        data_ingestion_config= config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion_output = data_ingestion.extract_zip_file()
         

# if __name__ == "__main__":
#     try:
#         logger.info(f"🏃‍➡️🏃‍➡️🏃‍➡️🏃‍➡️🏃‍➡️🏃‍➡️🏃‍➡️{STAGE_NAME}🏃‍➡️🏃‍➡️🏃‍➡️🏃‍➡️🏃‍➡️🏃‍➡️🏃‍➡️")
#         obj = DataingestionTrainingPipeline()
#         obj.initiate_dataingestion()
#         logger.info(f"🎉🎉🎉🎉🎉🎉{STAGE_NAME}🎉🎉🎉🎉🎉🎉🎉🎉🎉\n\n\n")

#     except Exception as e:
#         logger.exception(e)
#         raise e

