import sys

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v128 import io
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




driver = webdriver.Chrome()
driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")

def test_case_024():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()

    email = driver.find_element(By.ID, "input-email")
    password = driver.find_element(By.ID, "input-password")
    email.send_keys("phucpro2104@gmail.com")
    password.send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(2)
    # Truy cập vào trang sản phẩm và thêm sản phẩm vào giỏ hàng
    driver.get("http://localhost/opencart/index.php?route=product/product&product_id=40")

    # Nhấn nút "Thêm vào giỏ hàng"
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "button-cart"))
    )
    add_to_cart_button.click()
    time.sleep(10)

    # Đợi giỏ hàng được cập nhật và truy cập vào trang giỏ hàng
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "i.fa-solid.fa-cart-shopping"))
    ).click()
    time.sleep(2)
    # Kiểm tra số lượng trong giỏ hàng
    quantity_input = driver.find_element(By.CSS_SELECTOR, "input[name='quantity']")

    # Lấy giá trị của thuộc tính value trong trường input
    quantity_value = quantity_input.get_attribute("value")

    # Kiểm tra xem giá trị của số lượng có đúng không
    assert quantity_value == "1", f"Số lượng trong giỏ hàng không đúng. Expected: 1, Found: {quantity_value}"

    print(f"Số lượng trong giỏ hàng đúng: {quantity_value}")

    driver.quit()

def test_case_025():
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
    email = driver.find_element(By.ID, "input-email")
    email.send_keys("phucpro2104@gmail.com")
    password = driver.find_element(By.ID, "input-password")
    password.send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(2)

    driver.get("http://localhost/opencart/index.php?route=checkout/cart&language=en-gb")
    time.sleep(10)
    empty_cart_message = driver.find_element(By.CSS_SELECTOR, "#content p").text
    if "Your shopping cart is empty!" in empty_cart_message:
        print("The cart is already empty.")
        return

    while True:
        remove_buttons = driver.find_elements(By.CSS_SELECTOR, "button[formaction*='checkout/cart.remove']")
        if not remove_buttons:
            break

        for button in remove_buttons:
            try:
                button.click()
                time.sleep(2)
            except StaleElementReferenceException:
                break

    print("Vỏ hàng trống.")


def test_case_026( click_count=3):
    # Truy cập trang chủ
    driver.get("http://localhost/opencart/index.php?route=common/home&language=en-gb")

    time.sleep(2)
    wait = WebDriverWait(driver, 2)

    # tìm nút "Add to cart của Sản phẩm thứ 1"
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(2) > div > div.content > form > div > button:nth-child(1)")))
    time.sleep(2)

    # Kéo Scroll xuống và sau đó click nút "Add to cart"
    driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
    time.sleep(2)
    add_to_cart_button.click()
    time.sleep(2)

    driver.get("http://localhost/opencart/index.php?route=product/product&language=en-gb&product_id=43")  # Mở ra trang product của Macbook
    time.sleep(2)

    time.sleep(2)
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))  # Click vào nút "Add to cart"
    add_to_cart_button.click()
    time.sleep(7)

    cartButton = driver.find_element(By.CSS_SELECTOR, "#header-cart > div > button")
    # driver.execute_script("arguments[0].scrollIntoView(true);", cartButton) #Scroll xuống và nhấn vào nút chứ tổng sản phẩm và tổng tiền
    cartButton.click()
    time.sleep(2)

    # Tìm tên các sản phẩm
    productNames = driver.find_elements(By.CSS_SELECTOR,
                                        "#header-cart > div > ul > li > table > tbody > tr > td.text-start > a")
    actualProductNames = [name.text for name in productNames]

    expectedProductNames = ["iPhone", "MacBook"]

    assert sorted(expectedProductNames) == sorted(actualProductNames), "Tên sản phẩm không khớp"