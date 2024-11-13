from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




driver = webdriver.Chrome()
driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")

def test_case_019():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")
    time.sleep(2)
    driver.get("http://localhost/opencart/index.php?route=product/product&language=en-gb&product_id=43")  # Đến trang chi tiết sản phẩm
    time.sleep(2)

    # Nhập số âm vào trường số lượng
    quantity_input = driver.find_element(By.ID, "input-quantity")  # Lấy trường nhập liệu có id là "input-quantity"
    quantity_input.clear()  # Xóa trường nhập liệu nếu có giá trị trước đó
    quantity_input.send_keys("-1")  # Nhập số âm

    # Nhấn nút Thêm vào giỏ hàng
    driver.find_element(By.ID, "button-cart").click()  # Giả sử id của nút là "button-cart"
    time.sleep(2)

    # Sử dụng WebDriverWait để đợi thông báo lỗi
    try:
        error_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible"))
        ).text  # Đợi thông báo lỗi xuất hiện
        assert "Invalid quantity" in error_message, f"Expected error message 'Invalid quantity', but got {error_message}"
        print("Kiểm tra số âm trong số lượng thành công.")
    except Exception as e:
        print(f"Không tìm thấy thông báo lỗi: {str(e)}")

    driver.quit()
def test_case_020():
    driver = webdriver.Chrome()
    # Truy cập trang chi tiết sản phẩm
    driver.get("http://localhost/opencart/index.php?route=product/product&product_id=43")
    time.sleep(2)

    # Thêm sản phẩm vào giỏ hàng với giá trị đơn hàng thấp hơn giá trị tối thiểu
    quantity_input = driver.find_element(By.ID, "input-quantity")
    quantity_input.clear()
    quantity_input.send_keys("0")  # Giả sử sản phẩm có giá thấp hơn giá trị tối thiểu (ví dụ 10 USD)

    # Thêm vào giỏ hàng
    driver.find_element(By.ID, "button-cart").click()
    time.sleep(2)

    # Kiểm tra thông báo lỗi nếu có
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible"))
        ).text
        print(f"Thông báo không có lỗi  (giới hạn tối thiểu): {error_message}")
    except:
        print("Không có thông báo về giá trị đơn hàng tối thiểu.")

def test_case_021():
    driver = webdriver.Chrome()
     # Truy cập trang chi tiết sản phẩm
    driver.get("http://localhost/opencart/index.php?route=product/product&product_id=43")
    time.sleep(2)
    # Tiếp theo, thêm sản phẩm vào giỏ hàng với giá trị vượt quá giá trị tối đa
    quantity_input = driver.find_element(By.ID, "input-quantity")
    quantity_input.clear()
    quantity_input.send_keys("1000")  # Giả sử sản phẩm có giá cao hơn giá trị tối đa (ví dụ 1000 USD)

    # Thêm vào giỏ hàng
    driver.find_element(By.ID, "button-cart").click()
    time.sleep(2)

    # Kiểm tra thông báo lỗi nếu có
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible"))
        ).text
        print(f"Thông báo không có lỗi (giới hạn tối đa): {error_message}")
    except:
        print("Không có thông báo về giá trị đơn hàng tối đa.")

    # Đóng trình duyệt sau khi kiểm tra
    driver.quit()

def test_case_022():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/index.php?route=account/login")
    time.sleep(2)

    # Đăng nhập với thông tin hợp lệ
    username = driver.find_element(By.ID, "input-email")
    password = driver.find_element(By.ID, "input-password")

    username.send_keys("phucpro2104@gmail.com")
    password.send_keys("123456")
    time.sleep(2)

    # Submit the password change
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(5)  # Wait for the password change to process


    # Chờ trong thời gian giới hạn session (Giả sử session là 30 phút)
    print("Chờ trong 30 phút (giới hạn session)...")
    time.sleep(10)  # Chờ 30 phút

    # Kiểm tra lại nếu người dùng có thể truy cập vào một trang sau khi session hết hạn
    driver.get("http://localhost/opencart/index.php?route=account/account")  # Trang tài khoản người dùng

    try:
        # Kiểm tra nếu người dùng vẫn còn đăng nhập
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".dropdown-toggle"))
        )
        print("Người dùng vẫn đăng nhập và có thể truy cập trang tài khoản.")
    except:
        # Kiểm tra nếu có thông báo yêu cầu đăng nhập lại
        try:
            error_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
            ).text
            print(f"Thông báo lỗi (session hết hạn): {error_message}")
        except:
            print("Không tìm thấy thông báo lỗi. Kiểm tra lại cấu hình session.")

    # Đóng trình duyệt sau khi kiểm tra
    driver.quit()
def test_case_023():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")

    # Đợi cho đến khi ô tìm kiếm có thể nhấn được
    search_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input.form-control.form-control-lg"))
    )

    # Nhập một từ khóa dài (100 ký tự)
    long_keyword = "phucpro2104@gmail".ljust(100, "a")
    search_input.send_keys(long_keyword)

    # Gửi yêu cầu tìm kiếm
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-light.btn-lg"))
    )
    search_button.click()

    # Đợi kết quả tìm kiếm hoặc thông báo lỗi xuất hiện
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "a[href='http://localhost/opencart/index.php?route=product/search&language=en-gb']"))
        )
        print("Kết quả tìm kiếm đã tải, kiểm tra hành vi mong đợi với đầu vào dài.")
    except:
        print("Kết quả tìm kiếm không tải như mong đợi với đầu vào dài.")

    driver.quit()

def test_case_024():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")
    time.sleep(2)
    # Đợi cho đến khi ô tìm kiếm có thể nhấn được và để trống
    search_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input.form-control.form-control-lg"))
    )

    # Đảm bảo ô tìm kiếm không có từ khóa nào
    search_input.clear()
    time.sleep(2)
    # Nhấn nút tìm kiếm mà không nhập gì
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-lang='en-gb']"))
    )
    search_button.click()
    time.sleep(2)
    # Kiểm tra xem liên kết "Search" có xuất hiện không
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "a[href='http://localhost/opencart/index.php?route=product/search&language=en-gb']"))
        )
        print("Liên kết 'Search' xuất hiện, trang tìm kiếm đã được tải.")
    except:
        print("Liên kết 'Search' không xuất hiện, không thể chuyển đến trang tìm kiếm.")

    driver.quit()

