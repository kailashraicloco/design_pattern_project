import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

class GetEnv:
    def __init__(self):
        pass
    @classmethod
    def get_env(cls,env_variable_name):
        return os.getenv(env_variable_name)