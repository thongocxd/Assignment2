from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def get_firefox_driver_with_custom_user_agent(profile_path):
    options = Options()
    options.add_argument(f"--user-data-dir={profile_path}")  # Setting user data dir for Firefox
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
    options = Options()
    options.add_argument(f"-profile")
    options.add_argument(profile_path)
    return Firefox(service=Service(GeckoDriverManager().install()), options=options)
