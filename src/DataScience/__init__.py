import os
import sys
import logging
from datetime import datetime

log_dir = "Logs"
log_file_path = os.path.join(log_dir,"logging.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(         #"easy button" for setting up logging
    level=logging.INFO,
    format= "%(asctime)s: %(levelname)s: %(name)s: %(message)s",

    handlers = [
        logging.FileHandler(log_file_path,  mode='a'), ## message will be show in file_path 
        logging.StreamHandler(sys.stdout)   ## message will be shown in console also
    ]
),

logger = logging.getLogger(__name__)                    ##2025-09-29 08:55:44,838: INFO: src.DataScience: checking cheking ......
# logger = logging.getLogger("Data-Science-logger")     ##2025-09-29 08:56:15,677: INFO: Data-Science-logger: checking cheking .....



