from os.path import abspath, dirname, join
from os import environ
import dotenv


class ScrapingSettings:
    """General web scraping configurations."""
    TARGET_URL = environ.get(
        'SCRAPING_TARGET_URL',
        'http://sigtap.datasus.gov.br/tabela-unificada/app/sec/procedimento/publicados/consultar'
    )
    NUM_PAGES = int(environ.get('SCRAPING_NUM_PAGES', '56'))
    WAIT_TIME = int(environ.get('SCRAPING_WAIT_TIME', '3'))


class SelectorSettings:
    """Selector configurations (XPaths, IDs, CSS classes)."""
    ID_ACCESS_URL = environ.get('SCRAPING_ID_ACCESS_URL', 'acessoAutomatico')
    ID_GROUP_DROPDOWN = environ.get('SCRAPING_ID_GROUP_DROPDOWN', 'formConsultarProcedimento:grupo')
    GROUP_07_OPTION_VALUE = environ.get('SCRAPING_GROUP_07_OPTION_VALUE', '5')
    ID_SEARCH_BUTTON = environ.get('SCRAPING_ID_SEARCH_BUTTON', 'formConsultarProcedimento:localizar')
    XPATH_RESULTS_TABLE = environ.get(
        'SCRAPING_XPATH_RESULTS_TABLE',
        "//*[@id='formConsultarProcedimento:historicoProcedimento:tbody_element']"
    )
    XPATH_NEXT = environ.get(
        'SCRAPING_XPATH_NEXT',
        "//*[@id='formConsultarProcedimento']/table[3]/tbody/tr/td[4]"
    )
    LOADING_OVERLAY_CLASS = environ.get('SCRAPING_LOADING_OVERLAY_CLASS', 'ui-datatable-loading')
    CELL_NAME_CLASS = environ.get('SCRAPING_CELL_NAME_CLASS', 'nomeMed')


class ChromeSettings:
    """Chrome WebDriver configurations."""
    HEADLESS = environ.get('CHROME_HEADLESS', 'true').lower() == 'true'
    WINDOW_SIZE = environ.get('CHROME_WINDOW_SIZE', '1920,1080')
    USER_AGENT = environ.get(
        'CHROME_USER_AGENT',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    )
    NO_SANDBOX = environ.get('CHROME_NO_SANDBOX', 'true').lower() == 'true'
    DISABLE_DEV_SHM_USAGE = environ.get('CHROME_DISABLE_DEV_SHM_USAGE', 'true').lower() == 'true'
    DISABLE_GPU = environ.get('CHROME_DISABLE_GPU', 'true').lower() == 'true'


class OutputSettings:
    """Output configurations for collected data."""
    FILE_NAME = environ.get('OUTPUT_FILE_NAME', 'opme_sigtap.json')
    ENCODING = environ.get('OUTPUT_ENCODING', 'utf-8')
    INDENT_JSON = int(environ.get('OUTPUT_INDENT_JSON', '4'))


class AppSettings:
    """General application configurations."""
    APP_NAME = "OPME Ingestion"
    ROOT_PATH = dirname(dirname(dirname(dirname(abspath(__file__)))))
    PROJECT_PATH = dirname(dirname(dirname(abspath(__file__))))
    LOGS_PATH = join(ROOT_PATH, "logs")
    ENV = environ.get('ENV', 'development')


class Settings:
    """Main class that groups all configurations."""
    dotenv.load_dotenv(dotenv.find_dotenv())
    app: AppSettings = AppSettings()
    scraping: ScrapingSettings = ScrapingSettings()
    selectors: SelectorSettings = SelectorSettings()
    chrome: ChromeSettings = ChromeSettings()
    output: OutputSettings = OutputSettings()

