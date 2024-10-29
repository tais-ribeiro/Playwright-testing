from playwright.sync_api import Playwright

def pytest_configure(config: Playwright):
    config.set_default_timeout(30000)

    config.project_dir = "tests" 

    config.use(
        browser_name="chromium",  
        headless=False,            
        viewport={"width": 1280, "height": 720},  
        ignore_https_errors=True, 
    )
