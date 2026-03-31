import os

# Environment variables
OLLAMA_API_URL = os.getenv('OLLAMA_API_URL', 'http://default-api-url.com')
OLLAMA_TIMEOUT = int(os.getenv('OLLAMA_TIMEOUT', 30))  # in seconds
DEFAULT_MODEL = os.getenv('DEFAULT_MODEL', 'default-model')
AVAILABLE_MODELS = os.getenv('AVAILABLE_MODELS', '').split(',')  # comma-separated list

# Logging configuration
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

# API settings
API_SETTINGS = {
    'retry_attempts': 3,
    'retry_delay': 5  # in seconds
}