from os.path import abspath, dirname, join
from os import environ
import dotenv


class AppSettings:
    APP_NAME = "Streamlit MVP"
    ROOT_PATH = dirname(dirname(dirname(dirname(abspath(__file__)))))
    PROJECT_PATH = dirname(dirname(dirname(abspath(__file__))))
    LOGS_PATH = join(ROOT_PATH, "logs")
    ENV = environ.get('ENV')
    
class CoreApiSettings:
    API_HOST = "http://localhost"
    API_PORT = "8000"
    API_URL = None
    
    def __post_init__(self):
        self.API_URL = f"{self.API_HOST}:{self.API_PORT}"

class Settings:
    dotenv.load_dotenv(dotenv.find_dotenv())
    app: AppSettings = AppSettings()
    api: CoreApiSettings = CoreApiSettings()
