import logging
import os
from datetime import datetime


def get_current_time():
    """Get the current time as a string."""
    return datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

def setup_logging():
    """Setup logging configuration to write logs to a file."""
    log_directory = 'logs'
    time=get_current_time()
    log_file = os.path.join(log_directory, f'{time}.log')

    # Ensure the logs directory exists
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    logging.basicConfig(
        filename=log_file,  # File to write logs to
        level=logging.INFO,  # Set logging level to INFO (can be DEBUG, WARNING, etc.)
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
        datefmt='%Y-%m-%d %H:%M:%S'  # Date format
    )


if __name__ == '__main__':
    setup_logging()

    logger = logging.getLogger(__name__)

    logger.info('Hello, World!')

    logger.warning('This is a warning!')