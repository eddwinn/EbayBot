from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


username = 'bobsuper-0'
password = 'julie774'


def login():

    options = Options()
    options.headless = True
    options.add_argument("-private")

    driver = webdriver.Firefox(options=options, executable_path="/home/bot/EbayBot/venv/lib/python3.5/geckodriver")
    driver.set_window_size(1280, 850)

    try:
        driver.get('https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.com%2F')

    except Exception as e:
        print(str(e))

    try:
        # LOGIN
        # get the form


        # login to form

        username_form = driver.find_element_by_name("userid")
        username_form.clear()
        username_form.send_keys(username)
        password_form = driver.find_element_by_name("pass")
        password_form.clear()
        password_form.send_keys(password)
        submit = driver.find_element_by_id("sgnBt")
        driver.save_screenshot('login-success.png')
        submit.click()

        time.sleep(5)
        print("logged in as: ", username)

    except Exception as e:
        driver.save_screenshot('login-failure.png')
        print(str(e))


