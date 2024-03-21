from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


# def browser_init(context, browser_name, headless=False):
#     if browser_name == 'chrome':
#         chrome_options = webdriver.ChromeOptions()
#         if headless:
#             chrome_options.add_argument('--headless')
#             chrome_options.add_argument("--window-size=1920x1080")
#         context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#         if not headless:
#             context.driver.maximize_window()
#     elif browser_name == 'firefox':
#         firefox_options = webdriver.FirefoxOptions()
#         if headless:
#             firefox_options.add_argument('--headless')
#             firefox_options.add_argument("--window-size=1920x1080")
#         context.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
#         if not headless:
#             context.driver.maximize_window()
#     else:
#         raise ValueError(f"Unsupported browser: {browser_name}.\nPlease use 'chrome' or 'firefox'.")
#
#     context.wait = WebDriverWait(context.driver, 10)
#     context.app = Application(context.driver)
#

def browser_init(context):
    user_name = ''
    access_key = ''
    browser_stack_url = f'http://{user_name}:{access_key}@hub-cloud.browserstack.com/wd/hub'
    options = Options()
    browser_stack_options = {
        'os': 'OS X',
        'osVersion': 'Ventura',
        'browserName': 'Chrome',
        'sessionName': 'Target Search'
    }
    options.set_capability('bstack:options', browser_stack_options)
    context.driver = webdriver.Remote(command_executor=browser_stack_url, options=options)

    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

def before_step(context, step):
    print('\nCurrent step: ', step.name)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step.name)

def after_scenario(context, scenario):
    print('\nEnded scenario: ', scenario.name)
    context.driver.delete_all_cookies()
    context.driver.quit()
