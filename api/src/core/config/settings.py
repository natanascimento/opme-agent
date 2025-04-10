from os.path import abspath, dirname, join
from os import environ
import dotenv


class DatabaseSettings:
    DB_TYPE = environ.get('DB_TYPE')
    DB_USER = environ.get('DB_USER')
    DB_PASSWORD = environ.get('DB_PASSWORD')
    DB_CLUSTER = environ.get('DB_CLUSTER')
    DB_APP_NAME = environ.get('DB_NAME')

class AppSettings:
    APP_NAME = "Agent API"
    ROOT_PATH = dirname(dirname(dirname(dirname(abspath(__file__)))))
    PROJECT_PATH = dirname(dirname(dirname(abspath(__file__))))
    LOGS_PATH = join(ROOT_PATH, "logs")
    ENV = environ.get('ENV')

class OpenAiSettings:
    AUTH_TOKEN = environ.get('OPENAI_AUTH_TOKEN')

class AgentSettings:
    SYSTEM_ROLE = """
        TBD
    """
    
class UserPreferences:
    preference: str = """
        TBD
    """

class Settings:
    dotenv.load_dotenv(dotenv.find_dotenv())
    app: AppSettings = AppSettings()
    database: DatabaseSettings = DatabaseSettings()
    agent: AgentSettings = AgentSettings()
    user: UserPreferences = UserPreferences()
    oai: OpenAiSettings = OpenAiSettings()
