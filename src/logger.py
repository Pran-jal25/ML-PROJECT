#all the info, execution in some file to track any error so we logged that in any text file:

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

#- "logs":- A string literal representing a subdirectory named logs. This is where log files are intended to be stored

os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


# The below code configures Python’s built-in logging module. It sets up how log messages will be written:
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# if __name__=="__main__":
#     logging.info("Logging has started")