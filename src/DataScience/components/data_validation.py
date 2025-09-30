import os
from src.DataScience import logger
import pandas as pd
from src.DataScience.config.configuration import DataValidation_config

class DataValiadtion:
    def __init__(self, config: DataValidation_config):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns) ##columns in data

            all_schema = self.config.all_schema.keys() ##columns according to us

            
            for col in all_cols:
                if col not in all_schema:  ## if data_columns not match with our_columns
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f"Validation status -> {col}: {validation_status} \n")

            if validation_status:
                validation_status = True
                with open(self.config.STATUS_FILE, 'a') as f:
                    f.write(f"All columns are valid. Validation status True. \n")

            return validation_status
        
        except Exception as e:
            raise e
        
    def validate_columns_type(self)-> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            data_col_dtype = data.dtypes  # This returns a Series

            validation_status = True  # Assume everything is valid unless we find an error

            for col, expected_dtype in self.config.all_schema.items():
                actual_dtype = str(data_col_dtype[col])

                if actual_dtype != expected_dtype:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f"Data type mismatch for column '{col}': expected {expected_dtype}, got {actual_dtype}\n Validation status -> : {validation_status} ")
                    break  # You can remove break if you want to log all mismatches

            if validation_status:
                with open(self.config.STATUS_FILE, 'a') as f:
                    f.write("All column data types are valid. Validation status True\n")

            return validation_status
        except Exception as e:
            raise e