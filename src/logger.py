import logging
import os
from datetime import datetime

# Step 1: Create a 'logs/' folder
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Step 2: Generate timestamped log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Step 3: Set up logging with handlers (file + console)
logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler()  # log to terminal
    ]
)

