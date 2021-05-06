from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time


def login_main(user, password):
    driver = webdriver.Chrome(executable_path='/Users/csardana/PycharmProjects/AutoLog/chromedriver 3')
    driver.get("http://gmail.com")
    driver.set_page_load_timeout(10)
    driver.maximize_window()

    username_input = driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    submit = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
    username_input.send_keys(user)
    submit.send_keys(Keys.RETURN)

    driver.set_page_load_timeout(5)
    password_input = driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    password_input.send_keys(password.strip())
    submit.send_keys(Keys.RETURN)

    driver.set_page_load_timeout(5)
    time.sleep(60)

def main():
    if len(sys.argv) != 4:
        print("Please provide service ,Email and Password as arguments")
    else:
        print("\n**** Login Initiated ****\n")
        email = sys.argv[2]
        password = sys.argv[3]
        login_main(email, password)


main()
