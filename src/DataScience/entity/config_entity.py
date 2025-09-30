
from dataclasses import dataclass
from pathlib import Path

### 📁(entry karni ha) entity/ → 🗂️ ONLY DEFINE data entities (e.g., input/output dataclasses, structured schemas).
@dataclass 
class DataIngestion_config:
    root_dir: Path
    url: str
    input_dir: Path
    output_dir: Path


### 📁 entity/ → 🗂️ ONLY DEFINE data entities (e.g., input/output dataclasses, structured schemas).
@dataclass 
class DataValidation_config:
    root_dir:Path
    STATUS_FILE:str
    unzip_data_dir:Path
    all_schema:dict


@dataclass()
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str

@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str