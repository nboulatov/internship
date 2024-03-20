from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC

class SettingsPage(BasePage):
    LOCATORS = {
        "Contact us": (By.CSS_SELECTOR, '.settings-block-menu [href="/contact-us"]'),
    }
    SOCIAL_GRID = (By.CSS_SELECTOR, '.social-grid')
    SOCIAL_MEDIA_ICONS = (By.CSS_SELECTOR, '.img-social')
    def click_settings_block_menu_button(self, button):
        locator = self.LOCATORS.get(button)
        self.wait_for_clickable_element_and_click(*locator)

    def verify_social_media_icons(self, number):
        icon_elements = self.driver.find_elements(*self.SOCIAL_MEDIA_ICONS)
        assert len(icon_elements) >= int(number), f"\nExpected: {number}. \nActual: {len(icon_elements)}."
