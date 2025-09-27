## Folder Structure of ML Project

import os 
from pathlib import Path
import logging

logging.basicConfig( level=logging.INFO, format="[%(asctime)s]: %(message)s:" )

project_name ="Data-Science"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",   ##__init__.py --> we can package entire src folder into package so that it can be imported

    f"src/{project_name}/components/__init__.py", ##components of pipeline like data-ingestion, data-migration .....etc

    f"src/{project_name}/utils/__init__.py", ##generic functionality used by entire project
    f"src/{project_name}/utils/common.py",

    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    f"src/{project_name}/pipeline/__init__.py",

    f"src/{project_name}/entity/__init__.py",  
    f"src/{project_name}/entity/config_entity.py",

    f"src/{project_name}/constants/__init__.py",  

    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "experiment/experiment.ipynb",
    "templates/index.html",

]

for filepath in list_of_files:
    filepath = Path(filepath)
    dir,file = os.path.split(filepath)
    print(dir,file)

    if dir != "":
          os.makedirs(dir,exist_ok=True)
          logging.info(f"Creating Directory {dir}")
        
    if (not os.path.exists(filepath)):
     with open (filepath, "w") as f:
          pass
          logging.info(f"Creating file {file}")

    else:
        logging.info(f"File -> {file} -> already exists.")