from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#CONSTANTS
WEB_DRIVER_PATH = "YOUR CHROME DRIVER.EXE PATH"
USERNAME_OR_EMAIL_NAME = "YOUR INSTA USER NAME"
LOGIN_PASSWORD = "YOUR INSTA LOGIN PASSWORD"
ID_TO_SEND = "YOUR INSTA ID TO SEND"
MESSAGE_TO_SEND = "YOUR MESSAGE TO SEND"


driver = webdriver.Chrome(WEB_DRIVER_PATH)
driver.get("https://www.instagram.com/")
time.sleep(2)
login = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
login.send_keys(USERNAME_OR_EMAIL_NAME)
word = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
word.send_keys(LOGIN_PASSWORD)
word.send_keys(Keys.ENTER)
time.sleep(10)
search = driver.find_element(By.CSS_SELECTOR, "._aauy")
search.send_keys(ID_TO_SEND)
time.sleep(3)
search.send_keys(Keys.ENTER)
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(7)

bt = driver.find_elements(By.CSS_SELECTOR, "._aa_m button")
bt2 = bt[1]
bt2.click()
time.sleep(5)
cancel = driver.find_elements(By.CSS_SELECTOR, "._a9-z button")
cancel2 = cancel[1]
cancel2.click()

box = driver.find_element(By.CSS_SELECTOR, "._acrb textarea")
box.send_keys(MESSAGE_TO_SEND)
box.send_keys(Keys.ENTER)
time.sleep(2)

