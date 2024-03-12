from behave import given, when, then


@then('I see URL contains text: {expected_text_in_url}')
def verify_page_url(context, expected_text_in_url):
    context.app.base_page.verify_page_url(expected_text_in_url)
