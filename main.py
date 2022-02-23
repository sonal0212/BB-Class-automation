from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from timetable import time_table
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from datetime import datetime

chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--disable-user-media-security=true")
chrome_options.add_argument("C:/Program Files/Google/Chrome")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://cuchd.blackboard.com/")

now = datetime.today()
curr_day, curr_hour, curr_min = now.strftime("%A %H %M").split()  # %A:-days %H:-24 hr system %M:-60min system
curr_hour = int(curr_hour)
curr_min = int(curr_min)
print(curr_hour,curr_min)
tt = time_table[curr_day]

try:
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, "button-1")))
    # This waits up to 10 seconds before throwing a TimeoutException unless
    # it finds the element to return within 10 seconds.WebDriverWait by
    # default calls the ExpectedCondition every 500 milliseconds until it returns successfully.
    popup = driver.find_element(By.CLASS_NAME, "button-1")
    popup.click()
    uid_ele = driver.find_element(By.NAME, "user_id")
    uid_ele.send_keys("20BCS1384")
    password_ele = driver.find_element(By.NAME, "password")
    password_ele.send_keys("Naman@12")
    password_ele.send_keys(Keys.ENTER)
    weekly_time_table = []
    for link, start_hour, start_min in tt:
        if start_hour == curr_hour and start_min-5 < curr_min < start_min+5:
            driver.get(link)
            print("congrats you are inside the class sonal,u can relax")
            break
        else:
            print("Oops! class not found")
    # test = "https://cuchd.blackboard.com/ultra/courses/_54190_1/outline"
    # driver.get(test)
    # drop_down = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, "sessions-list-dropdown")))
    # drop_down.click()
    # # wait for 10sec before giving error
    # room = driver.find_element(By.ID, "sessions-list")
    # room.click()
    # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.CLASS_NAME, "close")))
    # close_btn = driver.find_element(By.CLASS_NAME, "close")
    # close_btn.click()
except TimeoutException as error:
    print("Class Not Found")

time.sleep(2400)  # 40*60=2400
driver.close()