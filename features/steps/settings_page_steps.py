from behave import given, when, then


@when('I click on button: {button}')
def click_settings_block_menu_button(context, button):
    context.app.settings_page.click_settings_block_menu_button(button)

@then('I verify number of social media icons: {number}')
def verify_social_media_icons(context, number):
    context.app.settings_page.verify_social_media_icons(number)