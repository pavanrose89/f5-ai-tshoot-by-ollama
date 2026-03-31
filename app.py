import logging
import json
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CustomError(Exception):
    pass

class Configuration:
    def __init__(self, config_file):
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            logger.error(f"Configuration file not found: {self.config_file}")
            raise CustomError("Configuration file not found.")
        with open(self.config_file) as f:
            self.config = json.load(f)
            logger.info("Configuration loaded successfully.")

    def get(self, key):
        return self.config.get(key)

class InputValidator:
    @staticmethod
    def validate_input(user_input):
        if not user_input:
            logger.warning("Received empty input.")
            raise ValueError("Input cannot be empty.")
        # Add more input validation rules as necessary.
        return True

class ModelSelector:
    def select_model(self, model_name):
        available_models = self.get_available_models()
        if model_name not in available_models:
            logger.error(f"Model '{model_name}' not found.")
            raise CustomError(f"Model '{model_name}' selection error.")
        logger.info(f"Model '{model_name}' selected.")
        return model_name

    @staticmethod
    def get_available_models():
        return ['model_a', 'model_b', 'model_c']  # Example models

class App:
    def __init__(self, config_file):
        self.config = Configuration(config_file)
        self.validator = InputValidator()
        self.model_selector = ModelSelector()

    def run(self, user_input, model_name):
        try:
            self.validator.validate_input(user_input)
            selected_model = self.model_selector.select_model(model_name)
            # Implement your processing logic here
            logger.info(f"Running with model: {selected_model} and input: {user_input}")
            # Add functionality for progress indicators and streaming responses.
            return f"Processed input '{user_input}' with model '{selected_model}'."
        except CustomError as ce:
            logger.error(f"CustomError: {str(ce)}")
            return str(ce)
        except Exception as e:
            logger.error(f"An unexpected error occurred: {str(e)}")
            return "An unexpected error occurred."

if __name__ == '__main__':
    app = App(config_file='config.json')
    user_input = 'Sample input'  # Replace this with actual user input handling
    model_name = 'model_a'  # Replace this with actual model selection
    result = app.run(user_input, model_name)
    print(result)