import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from custom_user_firefox import get_firefox_driver_with_custom_user_agent

# Initialize the Firefox driver with the specified user agent and profile
driver = get_firefox_driver_with_custom_user_agent('my_firefox_profile')

# Navigate to the OpenCart demo site
driver.get("https://demo.opencart.com/")

try:
    # Wait for the "My Account" element to be clickable and then click it
    my_account = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))
    )
    my_account.click()

    # Wait for the "Login" link to be clickable and then click it
    login_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
    )
    login_link.click()

    # Wait for the email input field to be visible
    email = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "input-email")))
    password = driver.find_element(By.ID, "input-password")

    # Enter login credentials
    email.send_keys("test@example.com")
    password.send_keys("password123")

    # Click the login button
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # Check for successful login by waiting for the "Logout" link
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
        print("Đăng nhập thành công!")  # Successful login
    except Exception as e:
        print("Đăng nhập thất bại!", e)  # Failed login message

except Exception as e:
    print(f"Lỗi: {e}")  # General error handling

# Pause to see the result before closing the browser
time.sleep(15)

# Close the browser
driver.quit()
