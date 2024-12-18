from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




driver = webdriver.Chrome()
driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")

def test_case_014_navigate_to_homepage():
    driver=webdriver.Chrome()
    driver.get("http://localhost/opencart/index.php?route=checkout/cart&language=en-gb")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "img.img-fluid").click()
    time.sleep(5)
    # Kiểm tra URL để xác nhận quay về trang chủ
    assert driver.current_url == "http://localhost/opencart/index.php?route=common/home&language=en-gb", "Không quay lại trang chủ thành công"
    print("Đã trở về trang chủ thành công")
    driver.quit()


def test_case_015_navigate_to_product_page():
        driver = webdriver.Chrome()
        driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")
        time.sleep(2)

        # Điều hướng đến trang sản phẩm thông qua URL
        product_url = "http://localhost/opencart/index.php?route=product/product&language=en-gb&product_id=43"
        driver.get(product_url)

        time.sleep(2)

        # Kiểm tra URL để xác nhận điều hướng thành công
        assert "product_id=43" in driver.current_url, "Không điều hướng đến trang chi tiết sản phẩm MacBook thành công"
        print("Đã điều hướng đến trang sản phẩm MacBook thành công")

        driver.quit()


def test_case_016_navigate_main_menu():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")
    time.sleep(2)

    # Mục menu cần kiểm tra với link "Show All"
    menu_items = [
        ("Desktops", "Show All Desktops",
         "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=20"),
        ("Laptops & Notebooks", "Show All Laptops & Notebooks",
         "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=18"),
        ("Components", "Show All Components",
         "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=25")
    ]

    for item, show_all_text, show_all_link in menu_items:
        # Nhấp vào mục menu
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, item))).click()
        time.sleep(2)

        # Kiểm tra nếu chúng ta có thể thấy nút "Show All" và nhấp vào nó, hoặc điều hướng trực tiếp theo link
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, show_all_text))).click()
        time.sleep(2)

        # Kiểm tra URL để xác nhận điều hướng thành công
        assert show_all_link == driver.current_url, f"Không điều hướng đúng đến {item}. URL hiện tại: {driver.current_url}"
        print(f"Đã điều hướng và nhấp vào {item} thành công.")

    driver.quit()


def test_case_017_login_and_navigate_to_cart():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
    email = driver.find_element(By.ID, "input-email")
    password = driver.find_element(By.ID, "input-password")
    email.send_keys("phucpro2104@gmail.com")
    password.send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(2)

    # Bước 4: Điều hướng đến sản phẩm và thêm vào giỏ hàng
    driver.get(
        "http://localhost/opencart/index.php?route=product/product&language=en-gb&product_id=43")  # Thay bằng sản phẩm thực tế
    time.sleep(2)

    # Thêm sản phẩm vào giỏ hàng
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "button-cart"))).click()
    time.sleep(10)


    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "i.fa-solid.fa-cart-shopping"))).click()
    time.sleep(2)
    assert "cart" in driver.current_url, f"Không điều hướng đúng đến trang giỏ hàng. URL hiện tại: {driver.current_url}"
    print("Đã điều hướng đến trang giỏ hàng thành công.")

    driver.quit()

def test_case_018_navigate_to_checkout():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
    email = driver.find_element(By.ID, "input-email")
    password = driver.find_element(By.ID, "input-password")
    email.send_keys("phucpro2104@gmail.com")
    password.send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "i.fa-solid.fa-cart-shopping"))).click()
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-primary"))).click()
    time.sleep(2)
    assert "checkout" in driver.current_url, f"Không điều hướng đúng đến trang thanh toán. URL hiện tại: {driver.current_url}"
    print("Đã điều hướng đến trang thanh toán thành công.")
    driver.quit()