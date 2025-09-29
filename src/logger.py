import os
import logging
from datetime import datetime

logs_dir = os.path.join(os.getcwd,"logs")

os.makedirs(logs_dir,exist_ok=True)
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_file_path = os.path.join(logs_dir,log_file)

logging.basicConfig(
    filename=log_file_path,
    format='[%(asctime)s: %(levelname)s: %(module)s: %(message)s]',
    level=logging.INFO
)