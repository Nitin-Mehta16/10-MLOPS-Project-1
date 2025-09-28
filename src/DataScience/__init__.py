import os
import sys
import logging


log_dir = "Logs"
log_file_path = os.path.join(log_dir,"logging.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(         #"easy button" for setting up logging
    level=logging.INFO,
    format= "%(asctime)s: %(levelname)s: %(name)s: %(message)s",

    handlers = [
        logging.FileHandler(log_file_path), ## message will be show in file_path 
        logging.StreamHandler(sys.stdout)   ## message will be shown in console also
    ]
),

logger = logging.getLogger(__name__)

