from behave import given, when, then
from features.environment import browser_init


# @given('I use browser options: {browser_options}')
# def initialize_browser(context, browser_options):
#     options = browser_options.split(" ")
#     browser_name = options[0]
#     headless = 'headless' in options
#     browser_init(context, browser_name, headless)

@given('I navigate to: {url}')
def open_google(context, url):
    context.app.base_page.open(url)

@then('I see URL contains text: {expected_text_in_url}')
def verify_page_url(context, expected_text_in_url):
    context.app.base_page.verify_page_url(expected_text_in_url)
