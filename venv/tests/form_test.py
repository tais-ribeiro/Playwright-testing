from playwright.sync_api import sync_playwright
from utils.data_generator import generate_random_data
from pages.form_page import FormPage
import time

def run_test():
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://phptravels.com/demo/")
            
            data = generate_random_data()

            form_page = FormPage(page)

            form_page.fill_form(data)
            form_page.select_random_country()
            form_page.fill_result()

            form_page.submit_form()
            time.sleep(30)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        finally:
            browser.close()

if __name__ == "__main__":
    run_test()
