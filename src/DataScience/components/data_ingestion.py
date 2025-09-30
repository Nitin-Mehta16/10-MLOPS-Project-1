## 📁 components/ → 🧩 Reusable building blocks (e.g., data ingestion, preprocessing, training, evaluation). Each  script handles one major step.

import os
import urllib.request as request
from src.DataScience import logger
import zipfile
from src.DataScience.entity.config_entity import DataIngestion_config



class DataIngestion:
    def __init__(self,config: DataIngestion_config):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.input_dir):
            filename, headers = request.urlretrieve(
                url = self.config.url,
                filename = self.config.input_dir
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists")

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.output_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.input_dir, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
