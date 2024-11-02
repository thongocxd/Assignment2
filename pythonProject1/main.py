import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from custom_user_agent import get_chrome_driver_with_custom_user_agent

driver = get_chrome_driver_with_custom_user_agent('/my_profile')
# Điều hướng đến trang OpenCart
driver.get("https://demo.opencart.com/")

# Chờ phần tử "My Account" xuất hiện và nhấp vào nó
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()

# Chờ phần tử "Login" xuất hiện và nhấp vào nó
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
time.sleep(120)  # Tạm dừng để xem trang

# Điền thông tin đăng nhập
email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "input-email")))
password = driver.find_element(By.ID, "input-password")

email.send_keys("test@example.com")
password.send_keys("password123")

# Nhấp vào nút đăng nhập
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

# Kiểm tra kết quả đăng nhập
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
    print("Đăng nhập thành công!")
except:
    print("Đăng nhập thất bại!")

# Đóng trình duyệt
driver.quit()