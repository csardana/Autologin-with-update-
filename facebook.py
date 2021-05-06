from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time


def login_main(user, password):
    driver = webdriver.Chrome(executable_path='/Users/csardana/PycharmProjects/AutoLog/chromedriver 3')
    driver.get("http://facebook.com")
    driver.set_page_load_timeout(10)
    driver.maximize_window()

    username_input = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
    password_input = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/input")
    submit = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div["
                                          "2]/button")
    username_input.send_keys(user)
    password_input.send_keys(password.strip())
    driver.set_page_load_timeout(5)
    submit.send_keys(Keys.RETURN)
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
