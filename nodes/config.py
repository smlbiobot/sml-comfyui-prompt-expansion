import os
import configparser

class Config:
    def __init__(self):
        self.api_token = None
        self.set_api_token()

    def set_api_token(self):
        if self.api_token is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            parent_dir = os.path.dirname(current_dir)
            config_path = os.path.join(parent_dir, "config.ini")

            config = configparser.ConfigParser()
            config.read(config_path)

            try:
                deepseek_token = config['API']['DEEPSEEK_API_TOKEN']
                self.api_token = deepseek_token
            except KeyError:
                print("Error: DEEPSEEK_API_TOKEN not found in config.ini")