from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context, browser_name, headless=False):
    if browser_name.lower() == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument('--headless')
        context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    elif browser_name.lower() == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        if headless:
            firefox_options.add_argument('--headless')
        context.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}.\nPlease use 'chrome' or 'firefox'.")

    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_name = context.config.userdata.get('browser', 'chrome')
    browser_init(context, browser_name)

def before_step(context, step):
    print('\nStarted step: ', step.name)

def after_step(context, step):
    if step.status == 'failed':
        # context.driver.save_screenshot(f"{step.name}_test.png")
        print('\nStep failed: ', step.name)

def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
