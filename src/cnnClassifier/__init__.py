import os
import sys
import logging

# format for log messages
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Directory where log files will be stored
log_dir = "logs"
#  Full path to the log file where log entries will be written
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Sets the logging level to INFO. This means that INFO, WARNING, ERROR, and CRITICAL messages will be logged, but DEBUG messages will not be
logging.basicConfig(
    level= logging.INFO,
    # Uses the previously defined format string for log messages
    format= logging_str,
    # Defines how and where the log messages will be output
    handlers=[
        # Writes log messages to the specified log file.
        logging.FileHandler(log_filepath),
        # Writes log messages to the console (standard output)
        logging.StreamHandler(sys.stdout)
    ]
)
# Creates a logger object named "cnnClassifierLogger"
logger = logging.getLogger("cnnClassifierLogger")