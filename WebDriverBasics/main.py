# INTRO-1
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome(executable_path="C:\\Users\\Aakash Garg\\Desktop\\Github\\Learn Selenium\\Drivers\\chromedriver.exe")
# driver.get("https://www.google.com")

# print(driver.title)
# print(driver.current_url)
# print(driver.page_source)
# time.sleep(5)
# driver.quit()

# INTRO-2 - NAVIGATION
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome(executable_path="C:\\Users\\Aakash Garg\\Desktop\\Github\\Learn Selenium\\Drivers\\chromedriver.exe")
# driver.get("https://www.google.com")
# print(driver.title)
# print(driver.current_url)
# time.sleep(3)
# driver.get("https://www.facebook.com")
# print(driver.title)
# print(driver.current_url)
# time.sleep(3)
# driver.back()
# time.sleep(3)
# print(driver.title)
# driver.quit()

# INTRO- 3 - CONDITIONAL COMMANDS
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# driver = webdriver.Chrome(executable_path="C:\\Users\\Aakash Garg\\Desktop\\Github\\Learn Selenium\\Drivers\\chromedriver.exe")
# driver.get("https://www.google.com")
# print(driver.title)
# print(driver.current_url)
# ele = driver.find_element_by_name("q")
# print(ele.is_displayed())
# print(ele.is_selected())
# print(ele.is_enabled())
# driver.quit()

# WAITS - IMPLICIT AND EXPLICIT
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path="C:\\Users\\Aakash Garg\\Desktop\\Github\\Learn Selenium\\Drivers\\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://www.udemy.com/join/signup-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fjoin%2Flogin-popup%2F%3Flocale%3Den_US%26next%3Dhttps%253A%252F%252Fwww.udemy.com%252F%26response_type%3Dhtml")
# driver.implicitly_wait(10)
# # assert "Udemy" in driver.title
# name = driver.find_element_by_name("fullname").send_keys("Aakash Garg")
# email = driver.find_element_by_name("email").send_keys("aakashgarg289@gmail.com")
# password = driver.find_element_by_name("password").send_keys("A@k@$#@Udemy.")
# name = driver.find_element_by_name("submit").click()
# driver.quit()

# EXPLICIT WAIT
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\Aakash Garg\\Desktop\\Github\\Learn Selenium\\Drivers\\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.expedia.com/")
zero = driver.find_element_by_class_name("uitk-faux-input").click()
one = driver.find_element_by_id("location-field-destination-input").send_keys("Delhi")
one.Keys.RETURN
time.sleep(5)
driver.quit()