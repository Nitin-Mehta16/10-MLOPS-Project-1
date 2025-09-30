##generic functionality used by entire project

import os 
import yaml
from src.DataScience import logger
import json
import joblib  ## save model 
# from ensure import ensure_annotation
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


# @ensure_annotations ## AVOID/STRICT RULE FOR THIS --> [[ normaly "" def mul(x:int,y:int) "" --> we can give x and y any variable type(str,int....) ]]
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        path_to_yaml = os.path.abspath(str(path_to_yaml))
        print(f"Trying to load YAML from: {path_to_yaml}")  # DEBUG
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content) ## content["key1"] = value1, content.key1 => error, ConfigBox(content).key1 = value1 
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        logger.error(f"Error reading YAML: {e}")
        raise e


# @ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create dir from list of directories"""
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


# @ensure_annotations
def save_json(path: Path, data: dict):
    """save json data"""
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




# @ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data"""
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


# @ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file / model
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"model/binary file saved at: {path}")


# @ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data"""
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data
