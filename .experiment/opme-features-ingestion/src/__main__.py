import time
import json
import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

from src.core.config import settings
from src.core.logging import logger


def initialize_headless_driver():
    """Configures and starts Chrome WebDriver in headless mode with robust options."""
    logger.info("Starting Chrome WebDriver in headless mode...")
    
    chrome_options = Options()
    
    if settings.chrome.HEADLESS:
        chrome_options.add_argument("--headless=new")
    
    if settings.chrome.NO_SANDBOX:
        chrome_options.add_argument("--no-sandbox")
    
    if settings.chrome.DISABLE_DEV_SHM_USAGE:
        chrome_options.add_argument("--disable-dev-shm-usage")
    
    if settings.chrome.DISABLE_GPU:
        chrome_options.add_argument("--disable-gpu")
    
    chrome_options.add_argument(f"--window-size={settings.chrome.WINDOW_SIZE}")
    chrome_options.add_argument(f"user-agent={settings.chrome.USER_AGENT}")
    
    driver = webdriver.Chrome(options=chrome_options)
    logger.info("WebDriver started successfully.")
    return driver

def perform_search(driver):
    """Selects group '07' and clicks the search button."""
    logger.info("Performing Group 07 selection...")
    try:
        access_url = WebDriverWait(driver, settings.scraping.WAIT_TIME).until(
            EC.element_to_be_clickable((By.ID, settings.selectors.ID_ACCESS_URL))
        )
        access_url.click()

        logger.debug("URL accessed.")
        
        dropdown_element = WebDriverWait(driver, settings.scraping.WAIT_TIME).until(
            EC.presence_of_element_located((By.ID, settings.selectors.ID_GROUP_DROPDOWN))
        )

        logger.debug("Dropdown found.")
        selector = Select(dropdown_element)
        selector.select_by_value(settings.selectors.GROUP_07_OPTION_VALUE)
        
        logger.info("Group 07 selected. Waiting for results...")

        search_button = WebDriverWait(driver, settings.scraping.WAIT_TIME).until(
            EC.element_to_be_clickable((By.ID, settings.selectors.ID_SEARCH_BUTTON))
        )
        search_button.click()
        logger.info("Search button clicked. Waiting for results...")

        WebDriverWait(driver, settings.scraping.WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, settings.selectors.XPATH_RESULTS_TABLE))
        )

        logger.info("Results table found.")
    except TimeoutException:
        logger.error("Timeout exceeded during selection or search.")
        raise
    except NoSuchElementException:
        logger.error("Dropdown element or search button not found.")
        raise

def extract_page_data(driver):
    """Extracts the code and name of all procedures on the current page."""
    page_data = []
    
    try:
        WebDriverWait(driver, settings.scraping.WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, settings.selectors.XPATH_RESULTS_TABLE))
        )

        logger.debug("Table found")
        
        rows = driver.find_elements(By.XPATH, f"{settings.selectors.XPATH_RESULTS_TABLE}/tr")

        logger.debug(f"Rows found: {len(rows)}")
        
        for row in rows:
            try:
                cells = row.find_elements(By.CLASS_NAME, settings.selectors.CELL_NAME_CLASS)
                
                if not cells:
                    continue

                procedure = {
                    "opme": cells[0].text.strip()
                }
                logger.debug(f"OPME found: {procedure['opme']}")

                page_data.append(procedure)
            except Exception as e:
                logger.debug(f"Table row could not be processed: {e}")
                pass

    except TimeoutException:
        logger.warning("No data rows found in table. Verify if the search returned results.")
    except NoSuchElementException:
        logger.error("Results table not found.")
    except Exception as e:
        logger.error(f"Unexpected error while extracting page data: {e}")
        return False

    return page_data

def click_next_page(driver):
    """Clicks the 'Next Page' button and waits for AJAX loading to complete."""
    try:
        next_page_button = WebDriverWait(driver, settings.scraping.WAIT_TIME).until(
            EC.element_to_be_clickable((By.XPATH, settings.selectors.XPATH_NEXT))
        )
        
        if 'ui-state-disabled' in next_page_button.get_attribute('class'):
            logger.info("Next page button disabled. Last page reached.")
            return False

        next_page_button.click()
        
        WebDriverWait(driver, settings.scraping.WAIT_TIME).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, settings.selectors.LOADING_OVERLAY_CLASS))
        )
        
        time.sleep(1)
        
        return True
    except TimeoutException:
        logger.warning("Timeout: Next page button not found or new page did not load.")
        return False
    except ElementClickInterceptedException:
        logger.debug("Element intercepted, retrying...")
        time.sleep(2)
        return click_next_page(driver)
    except Exception as e:
        logger.error(f"Unexpected error while clicking next page: {e}")
        return False


def write_to_datalake(data):
    """Writes collected data to the datalake bronze layer with date partitioning."""
    date_str = datetime.now().strftime("%d%m%Y")
    output_dir = os.path.join("..", "datalake", "bronze", "sigtap", date_str)
    
    try:
        os.makedirs(output_dir, exist_ok=True)
        
        file_path = os.path.join(output_dir, "opme_sigtap.json")
        
        with open(file_path, 'w', encoding=settings.output.ENCODING) as f:
            json.dump(data, f, ensure_ascii=False, indent=settings.output.INDENT_JSON)
        
        logger.info("---------------------------------------------------")
        logger.info("Scraping completed!")
        logger.info(f"Total procedures collected: {len(data)}")
        logger.info(f"Data saved to: {file_path}")
        logger.info("---------------------------------------------------")
        
        return file_path
    except Exception as e:
        logger.error(f"Error saving file: {e}", exc_info=True)
        raise


def run():
    """Main function that orchestrates the complete data collection flow."""
    driver = None
    all_data = []
    
    try:
        driver = initialize_headless_driver()
        driver.get(settings.scraping.TARGET_URL)
        logger.info(f"Navigating to: {settings.scraping.TARGET_URL}")

        perform_search(driver)

        current_page = 1
        while True:
            logger.info(f"Collecting data from Page {current_page}")
            
            data = extract_page_data(driver)

            logger.debug(f"Data extracted from page {current_page}: {len(data) if data else 0} records")
            
            if not data and current_page == 1:
                 logger.error("No data rows found after search. Verify selectors.")
                 break
            if not data and current_page > 1:
                 logger.warning("No data rows on this page. Stopping scraping.")
                 break
            
            all_data.extend(data)

            if current_page < settings.scraping.NUM_PAGES:
                 if not click_next_page(driver):
                    logger.info("Navigation ended or maximum number of pages reached.")
                    break
                 current_page += 1
            else:
                 logger.info(f"Limit of {settings.scraping.NUM_PAGES} pages reached. Ending.")
                 break
        
    except Exception as e:
        logger.critical(f"Critical error occurred during execution: {e}", exc_info=True)
        
    finally:
        if driver:
            driver.quit()
            logger.info("WebDriver closed.")
            
    write_to_datalake(all_data)


if __name__ == "__main__":
    run()