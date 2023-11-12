# ------------------------------Twitter Complaint Bot--------------------------------

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from passcode import USER_NAME, PASSWORD

CHROME_DRIVER_PATH = "../../../Downloads/chromedriver_win32/chromedriver.exe"


class TwitterComplaintBot:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.up_down_speed = []

    def speed_finder(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()

        time.sleep(3)
        all_cookies = self.driver.find_element(
            By.XPATH,
            '//*[@id="onetrust-accept-btn-handler"]'
        )
        all_cookies.click()

        time.sleep(2)
        go_button = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        )
        go_button.click()
        time.sleep(50)
        speeds = self.driver.find_elements(By.CSS_SELECTOR, "div .result-data span")

        for speed in speeds:
            self.up_down_speed.append(speed.text)

    def message_creator(self):
        message = "Hey Airtel! My internet is very slow. Download speed is just {} Mbps\
         and Upload speed is {} Mbps. @airtelindia FIX IT NOW!!!!".format(
            self.up_down_speed[2], self.up_down_speed[3]
        )
        return message

    def twitter_operator(self):
        try:
            not_now = self.driver.find_element(
                By.XPATH,
                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/\
                div[2]/div/div[2]/div/div[2]/div[2]/div[2]'
            )
            not_now.click()
        except NoSuchElementException:
            pass
        finally:
            if float(self.up_down_speed[2]) < 70 or float(self.up_down_speed[3]) < 70:
                self.twitter_login_bot()

    def twitter_login_bot(self):
        self.driver.get("https://twitter.com/")

        time.sleep(4)
        sign_in_button = self.driver.find_element(
            By.CSS_SELECTOR,
            'div .css-1dbjc4n.r-16y2uox a'
        )
        sign_in_button.click()

        time.sleep(4)
        input_username = self.driver.find_element(By.NAME, "text")
        input_username.send_keys(USER_NAME)

        time.sleep(3)
        next_button = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/\
            div/div/div[2]/div[2]/div/div/div/div[6]'
        )
        next_button.click()

        time.sleep(3)
        input_password = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/\
            div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div\
            [2]/div[1]/input'
        )
        input_password.send_keys(PASSWORD)

        time.sleep(2)
        log_in_button = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/\
            div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div'
        )
        log_in_button.click()

        time.sleep(7)
        self.tweet_composer()

    def tweet_composer(self):
        tweet_compose = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/\
            div[1]/div[3]/a'
        )
        tweet_compose.click()

        time.sleep(6)
        field_place = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/\
            div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/\
            div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/\
            div/div/div/div/div[2]/div/div/div/div/span/br'
        )
        time.sleep(2)
        field_place.send_keys("{}".format(self.message_creator()))

        time.sleep(1)
        tweet_button = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/\
            div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/\
            div/div/div[2]/div[4]'
        )
        tweet_button.click()


complaint_bot = TwitterComplaintBot()
complaint_bot.speed_finder()
complaint_bot.twitter_operator()
# This program should be executed every one hour in a cloud to check the speed
