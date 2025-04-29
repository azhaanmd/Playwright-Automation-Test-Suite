import logging
import os
from datetime import datetime

# Make sure the logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Create a unique log file name
log_file = f"logs/test_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Create logger
logger = logging.getLogger("TestLogger")
logger.setLevel(logging.DEBUG)

# Avoid adding handlers multiple times
if not logger.handlers:
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
