from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from timetable import time_table
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from datetime import datetime

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://cuchd.blackboard.com/")
driver.maximize_window()
time.sleep(2)

now = datetime.today()
today_date_time = now.strftime("%A %H %M %S").split()
curr_day, curr_hour, curr_min, curr_sec = today_date_time
tt = time_table[curr_day]

try:
    time.sleep(5)
    popup = driver.find_element(By.CLASS_NAME, "button-1")
    popup.click()
    uid_ele = driver.find_element(By.NAME, "user_id")
    uid_ele.send_keys("20BCS1384")
    password_ele = driver.find_element(By.NAME, "password")
    password_ele.send_keys("Naman@12")
    password_ele.send_keys(Keys.ENTER)
    time.sleep(5)
except TimeoutError as error:
    print('Failed')
time.sleep(200)
driver.close()