from playwright.sync_api import Page
import random

class FormPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_form(self, data):
        self.page.fill('input[name="first_name"]', data["first_name"])
        self.page.fill('input[name="last_name"]', data["last_name"])
        self.page.fill('input[name="whatsapp"]', data["phone_number"])
        self.page.fill('input[name="business_name"]', data["company_name"])
        self.page.fill('input[name="email"]', data["email"])

    def select_random_country(self):
        self.page.wait_for_selector('select[name="country_id"]')
        country_dropdown = self.page.locator('select[name="country_id"]')
        country_options = country_dropdown.locator('option')
        options_list = country_options.all()

        if options_list:
            random_option = random.choice(options_list)
            country_dropdown.select_option(value=random_option.get_attribute('value'))

    def fill_result(self):
        numb1_text = self.page.locator('span[id="numb1"]').inner_text()
        numb2_text = self.page.locator('span[id="numb2"]').inner_text()

        numb1 = int(numb1_text)
        numb2 = int(numb2_text)
        result = numb1 + numb2

        self.page.fill('input[id="number"]', str(result))

    def submit_form(self):
        self.page.click('button[id="demo"]')
