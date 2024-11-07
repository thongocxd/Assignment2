from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")



def test_case_001():
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()

    # Điền thông tin đăng nhập
    email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "input-email")))
    password = driver.find_element(By.ID, "input-password")

    email.send_keys("phucpro2104@gmail.com")
    password.send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    # Kiểm tra kết quả đăng nhập
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
        print("Đăng nhập thành công!")
    except:
        print("Đăng nhập thất bại!")
    time.sleep(5)

    driver.quit()

def test_case_002():
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()


    # Điện trang đăng nhập
    email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "input-email")))
    password = driver.find_element(By.ID, "input-password")

    email.send_keys("phucpro2104@gmail.com")
    password.send_keys("1234567")

    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

    # Kiểm tra kết quả đăng nhập
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
        print("Đăng nhập thành công!")
    except:
        print("Đăng nhập thất bại!")
    time.sleep(5)

    driver.quit()


def test_case_003():
    # Step 1: Log in to the account
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()

    # Fill in login details
    email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "input-email")))
    password = driver.find_element(By.ID, "input-password")
    email.send_keys("phucpro2104@gmail.com")
    password.send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

    # Ensure the login was successful before continuing
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
        print("Login successful, proceeding to logout.")

        # Step 2: Logout
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()
        print("Logout successful!")

    except:
        print("Login failed; cannot proceed with logout.")
    finally:
        time.sleep(5)
        driver.quit()


def test_case_004():
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
    incorrect_password = "wrongpassword"
    correct_password = "123456"  # Mật khẩu đúng
    max_attempts = 10  # Số lần thử tối đa

    for attempt in range(1, max_attempts + 1):
        email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "input-email")))
        password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "input-password")))

        # Nhập thông tin tài khoản
        email.clear()
        password.clear()
        email.send_keys("phuc1@gmail.com")  # Thay thế bằng email đã đăng ký

        # Thử mật khẩu sai hoặc đúng
        if attempt == max_attempts:
            print(f"Attempt {attempt}: Thử mật khẩu đúng.")
            password.send_keys(correct_password)
        else:
            print(f"Attempt {attempt}: Thử mật khẩu sai.")
            password.send_keys(incorrect_password)

        # Nhấp vào nút đăng nhập
        driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

        # Kiểm tra thông báo lỗi
        try:
            error_message = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "dirv.alert.alert-danger.alert-dismissible"))
            )
            print(f"Attempt {attempt}: {error_message.text}")
        except:
            print(f"Attempt {attempt}: Không có thông báo lỗi.")

        # Thêm thời gian chờ giữa các lần thử để tránh bị khóa tạm thời
        time.sleep(3)

    print("Hoàn thành kiểm tra số lần nhập mật khẩu sai.")
    driver.quit()
def test_case_005():
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")

    # Điều hướng đến trang đăng nhập
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
    # Nhấp vào liên kết quên mật khẩu
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Forgotten Password"))).click()
    # Nhập địa chỉ email
    email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "input-email")))
    email.send_keys("phucpro2104@gmail.com")  # Thay thế bằng email đã đăng ký
    # Nhấp vào nút gửi
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(5)
    # Kiểm tra thông báo thành công
    try:
        success_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible"))
        )
        assert "Success: Your password has been successfully updated." in success_message.text
        print("Kiểm tra thành công: Thông báo thành công hiển thị đúng.")
    except:
        print("Kiểm tra thất bại: Không hiển thị thông báo thành công.")
    finally:
        time.sleep(5)
        driver.quit()

def test_case_006():
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
    time.sleep(5)
    # Điều hướng đăng nhập
    email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "input-email")))
    password = driver.find_element(By.ID, "input-password")

    email.send_keys("phucpro2104@gmail.com")
    password.send_keys("123456")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(5)
    # Kiểm tra kết quả đăng nhập
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
        print("Đăng nhập thanh công!")
    except:
        print("Đăng nhập thất bại!")

    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Change your password"))).click()
    time.sleep(5)  # Wait for the page to load

    # Change the password (adjust element locators as necessary)
    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "input-password")))
    new_password_field = driver.find_element(By.ID, "input-confirm")

    password_field.send_keys("123456")  # Current password
    new_password_field.send_keys("123456")  # New password
    time.sleep(5)  # Wait for input

    # Submit the password change
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(5)  # Wait for the password change to process

    # Verify the password change
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")))  # Adjust based on success message
        print("Mật khẩu đã được thay đổi thành công!")  # Password change successful
    except:
        print("Thay đổi mật khẩu thất bại!")  # Password change failed

def test_case_007():

    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")

    # Điều hướng đến trang đăng nhập
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()

    # Nhập thông tin tài khoản bị khóa
    email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "input-email")))
    password = driver.find_element(By.ID, "input-password")

    email.send_keys("phuc1@gmail.com")  # Thay thế bằng email của tài khoản bị khóa
    password.send_keys("123456")  # Thay thế bằng mật khẩu phù hợp

    # Nhấp vào nút đăng nhập
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

    # Kiểm tra thông báo lỗi
    try:
        error_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "dirv.alert.alert-danger.alert-dismissible"))
        )
        print(f"Kiểm tra thành công: Hiển thị thông báo lỗi: {error_message.text}")
    except:
        print("Kiểm tra thất bại: Không hiển thị thông báo lỗi cho tài khoản bị khóa.")
    finally:
        time.sleep(5)
    driver.quit()
