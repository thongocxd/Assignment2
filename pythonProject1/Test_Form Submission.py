from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




driver = webdriver.Chrome()
driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")


def test_case_008():
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    frist_name = driver.find_element(By.ID, "input-firstname")

    last_name = driver.find_element(By.ID, "input-lastname")

    email = driver.find_element(By.ID, "input-email")

    password = driver.find_element(By.ID, "input-password")

    frist_name.send_keys("phuc")
    last_name.send_keys("pro")
    email.send_keys("phucpro7@gmail.com")
    password.send_keys("123456")
    time.sleep(5)
    # Chọn hộp kiểm chính sách quyền riêng tư
    driver.find_element(By.NAME, "agree").click()
    time.sleep(5)
    # Nhấp vào nút "Continue" để gửi biểu mẫu đăng ký
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(5)
    # Kiểm tra xem có điều hướng đến trang xác nhận thành công không
    try:
        # Tìm phần tử chứa tiêu đề đăng ký thành công
        success_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='content']/h1"))
        )

        # Kiểm tra nội dung của tiêu đề
        if success_message.text == "Your Account Has Been Created!":
            print("Đăng ký thành công:", success_message.text)
        else:
            print("Đăng ký thất bại.")
    except:
        print("Đăng ký thất bại hoặc không tìm thấy thông báo thành công.")
    finally:
        time.sleep(5)
    driver.quit()

def test_case_009():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Điền thông tin vào biểu mẫu với email không hợp lệ
    first_name = driver.find_element(By.ID, "input-firstname")
    last_name = driver.find_element(By.ID, "input-lastname")
    email = driver.find_element(By.ID, "input-email")
    password = driver.find_element(By.ID, "input-password")

    first_name.send_keys("Phuc")
    last_name.send_keys("Pro")
    email.send_keys("phucpro2gmail")  # Email sai định dạng (thiếu .com)
    password.send_keys("123456")

    # Chọn hộp kiểm chính sách quyền riêng tư
    driver.find_element(By.NAME, "agree").click()

    # Nhấp vào nút "Continue" để gửi biểu mẫu đăng ký
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

    # Kiểm tra xem có hiển thị thông báo lỗi cho email không hợp lệ
    try:
        error_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div#error-email.invalid-feedback.d-block"))
        )
        print("Thông báo lỗi email không hợp lệ:", error_message.text)
    except:
        print("Không tìm thấy thông báo lỗi cho email không hợp lệ.")
    finally:
        time.sleep(5)
        driver.quit()


def test_case_010():
    driver = webdriver.Chrome()
    # Khởi tạo Chrome WebDriver
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")

    # Chuyển tới trang đăng ký tài khoản
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Điền vào các trường của biểu mẫu
    driver.find_element(By.ID, "input-firstname").send_keys("a" * 33)  # Nhập tên dài hơn 32 ký tự
    driver.find_element(By.ID, "input-lastname").send_keys("TestLastName")
    driver.find_element(By.ID, "input-email").send_keys("example@test.com")
    driver.find_element(By.ID, "input-password").send_keys("123")  # Nhập mật khẩu ngắn hơn 4 ký tự
    time.sleep(5)
    # Nhấp chọn điều khoản và đăng ký
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

    # Chờ thông báo lỗi xuất hiện
    time.sleep(2)
    try:
        # Kiểm tra thông báo lỗi cho tên
        name_error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(), 'First Name must be between 1 and 32 characters!')]"))
        )
        print("Thông báo lỗi tên:", name_error.text)

        # Kiểm tra thông báo lỗi cho mật khẩu
        password_error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(), 'Password must be between 4 and 20 characters!')]"))
        )
        print("Thông báo lỗi mật khẩu:", password_error.text)
    except:
        print("Không tìm thấy thông báo lỗi cho tên hoặc mật khẩu.")
    finally:
        # Đóng trình duyệt
        driver.quit()
def test_case_011():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()

    email = driver.find_element(By.ID, "input-email")

    password = driver.find_element(By.ID, "input-password")

    email.send_keys("phucpro2104@gmail.com")
    password.send_keys("123456")

    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Address Book"))).click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "New Address"))).click()
    time.sleep(2)
    # Điền vào các trường của biểu mẫu
    driver.find_element(By.ID, "input-firstname").send_keys("Phuc")
    driver.find_element(By.ID, "input-lastname").send_keys("Pro")
    driver.find_element(By.ID, "input-company").send_keys("My Company")
    driver.find_element(By.ID, "input-address-1").send_keys("123 Đường Lê Lợi")
    driver.find_element(By.ID, "input-address-2").send_keys("Phường 3")
    driver.find_element(By.ID, "input-city").send_keys("Hồ Chí Minh")
    driver.find_element(By.ID, "input-postcode").send_keys("700000")
    (driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"))
    time.sleep(2)
    country_dropdown = driver.find_element(By.ID, "input-country")
    country_dropdown.click()
    country_dropdown.find_element(By.XPATH, "//option[contains(text(), 'Viet Nam')]").click()
    time.sleep(2)  # Chờ danh sách vùng tải xong
    region_dropdown = driver.find_element(By.ID, "input-zone")
    region_dropdown.click()
    region_dropdown.find_element(By.XPATH, "//option[contains(text(), 'Ho Chi Minh')]").click()

    # Nhấp vào nút "Continue" để lưu địa chỉ
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    # Kiểm tra xem địa chỉ đã được thêm thành công chưa
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible"))
        )
        print("Địa chỉ đã được thêm thành công:", success_message.text)
    except:
        print("Thêm địa chỉ thất bại hoặc không tìm thấy thông báo thành công.")
    finally:
        time.sleep(5)
        driver.quit()


def test_case_012():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")

    # Đăng nhập vào tài khoản
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()

    email = driver.find_element(By.ID, "input-email")
    password = driver.find_element(By.ID, "input-password")
    email.send_keys("phucpro2104@gmail.com")
    password.send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(2)

    # Mở Address Book và thêm địa chỉ mới
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Address Book"))).click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "New Address"))).click()
    time.sleep(2)

    # Điền thông tin vào biểu mẫu, bao gồm mã ZIP không hợp lệ
    driver.find_element(By.ID, "input-firstname").send_keys("Phuc")
    driver.find_element(By.ID, "input-lastname").send_keys("Pro")
    driver.find_element(By.ID, "input-company").send_keys("My Company")
    driver.find_element(By.ID, "input-address-1").send_keys("123 Đường Lê Lợi")
    driver.find_element(By.ID, "input-address-2").send_keys("Phường 3")
    driver.find_element(By.ID, "input-city").send_keys("Hồ Chí Minh")
    driver.find_element(By.ID, "input-postcode").send_keys("abc123")  # Mã ZIP không hợp lệ
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # Chọn quốc gia và vùng (state)
    country_dropdown = driver.find_element(By.ID, "input-country")
    country_dropdown.click()
    country_dropdown.find_element(By.XPATH, "//option[contains(text(), 'Viet Nam')]").click()
    time.sleep(2)

    region_dropdown = driver.find_element(By.ID, "input-zone")
    region_dropdown.click()
    region_dropdown.find_element(By.XPATH, "//option[contains(text(), 'Ho Chi Minh')]").click()

    # Nhấp vào nút "Continue" để lưu địa chỉ
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(2)

    # Kiểm tra thông báo lỗi cho mã ZIP không hợp lệ
    try:
        zip_error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(), 'Postcode does not appear to be valid!')]"))
        )
        print("Thông báo lỗi mã ZIP:", zip_error_message.text)
    except:
        print("Không tìm thấy thông báo lỗi cho mã ZIP.")
    finally:
        time.sleep(5)
        driver.quit()
def test_case_013():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()

    frist_name = driver.find_element(By.ID, "input-firstname")

    last_name = driver.find_element(By.ID, "input-lastname")

    email = driver.find_element(By.ID, "input-email")

    password = driver.find_element(By.ID, "input-password")

    frist_name.send_keys("phuc")
    last_name.send_keys("pro")
    email.send_keys("phucpro2104@gmail.com")
    password.send_keys("1234567")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # Chọn hộp kiểm chính sách quyền riêng tư
    driver.find_element(By.NAME, "agree").click()

    # Nhấp vào nút "Continue" để gửi biểu mẫu đăng ký
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

    # Kiểm tra xem có hiển thị thông báo lỗi cho email không hợp lệ
    try:
        error_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "dirv.alert.alert-danger.alert-dismissible"))
        )
        print("Thông báo lỗi email không hợp lệ:", error_message.text)
    except:
        print("Không tìm thấy thông báo lỗi cho email không hợp lệ.")
    finally:
        time.sleep(5)
        driver.quit()

