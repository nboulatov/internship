from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context, browser_name, headless=False):
    if browser_name == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("--window-size=1920x1080")
        context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        if not headless:
            context.driver.maximize_window()
    elif browser_name == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        if headless:
            firefox_options.add_argument('--headless')
            firefox_options.add_argument("--window-size=1920x1080")
        context.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
        if not headless:
            context.driver.maximize_window()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}.\nPlease use 'chrome' or 'firefox'.")


    context.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)

def before_step(context, step):
    print('\nCurrent step: ', step.name)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step.name)

def after_scenario(context, scenario):
    print('\nEnded scenario: ', scenario.name)
    context.driver.delete_all_cookies()
    context.driver.quit()
