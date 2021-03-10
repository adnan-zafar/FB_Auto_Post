from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = None


def image():
    image_bot = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.stjgntxs > input')))
# change the path for image
    image_bot.send_keys(r"C:\Users\AdnanAwan\Desktop\scraper.jpg")
    caption = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div > div.o8yuz56k div._1mf._1mj')))
    caption.send_keys(input(str("Write about image:  ")))
    post = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div > div.btwxx1t3.c4xchbtz.by2jbhx6')))
    post.click()


def login():
    log_email_mob = input(str("Enter email or Mobile Number:  "))
    log_pass = input(str("Enter password:  "))
    name_email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#email")))
    name_email.click()
    name_email.send_keys(log_email_mob)
    password_fb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#pass")))
    password_fb.click()
    password_fb.send_keys(log_pass)
    login_fb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div._6ltg > button')))
    login_fb.send_keys(Keys.ENTER)

# initiate the chrome browser


def initiate_browser():
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")

    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option(
        "excludeSwitches", ['enable-automation'])
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1
                                                     })
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), options=chrome_options)
    return driver


def main():
    global driver
    driver = initiate_browser()
    driver.get("https://www.facebook.com")
    login()
    image()
    driver.quit()


if __name__ == "__main__":
    main()
