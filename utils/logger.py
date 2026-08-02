from loguru import logger
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure logger
logger.add(
    "logs/ai_sdet.log",
    rotation="5 MB",
    retention="7 days",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)

def get_logger():
    return logger