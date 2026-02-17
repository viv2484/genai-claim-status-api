import logging
import json

logger = logging.getLogger("claims-api")
logger.setLevel(logging.INFO)

def log_info(message: str, **kwargs):
    log = {"level": "INFO", "message": message, **kwargs}
    logger.info(json.dumps(log))

def log_error(message: str, **kwargs):
    log = {"level": "ERROR", "message": message, **kwargs}
    logger.error(json.dumps(log))
