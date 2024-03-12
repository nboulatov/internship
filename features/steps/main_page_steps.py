from behave import given, when, then


@when('I click Menu Block button: {button}')
def click_menu_block_button(context, button):
    context.app.main_page.click_menu_block_button(button)

@then('I verify page is displayed: Main Page')
def verify_main_page(context):
    context.app.main_page.verify_main_page()

