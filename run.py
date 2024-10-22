from app import create_app
from config import setup_logging

logger = setup_logging()

app = create_app()

if __name__ == "__main__":

    try:
        app.run(host="0.0.0.0", port=80,debug=True)
    except Exception as e:
        logger.error(e)
        logger.error("Failed to start the application")