# from selenium import webdriver
# from selenium.webdriver.common import keys
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome(executable_path = "C:\\Users\\Aakash Garg\\Desktop\\Github\\Learn Selenium\\Drivers\\chromedriver.exe")
# driver.get("https://www.google.com")
# print(driver.title)
# print(driver.current_url)
# time.sleep(1)
# driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
# print(driver.title)
# print(driver.current_url)
# ele = driver.find_element_by_id("user-message").send_keys("Aakash is a good boy...")
# btn = driver.find_element_by_xpath("//*[@id='get-input']/button").click()
# time.sleep(3)
# ele2 = driver.find_element_by_id("sum1").send_keys(12)
# ele3 = driver.find_element_by_id("sum2").send_keys(12)
# btn2 = driver.find_element_by_xpath("//*[@id='gettotal']/button").click()
# time.sleep(5)
# driver.back()
# time.sleep(2)
# driver.close()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\Aakash Garg\\Desktop\\Github\\Learn Selenium\\Drivers\\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
time.sleep(2)
ele = driver.find_element_by_id("isAgeSelected")
time.sleep(3)
print(ele.is_selected())
ele.click()
print(ele.is_selected())
time.sleep(2)
ele2 = driver.find_element_by_xpath("//*[@id='easycont']/div/div[2]/div[2]/div[2]/div[1]/label/input")
ele2.click()
time.sleep(2)
print(ele2.is_selected())
time.sleep(5)
btn = driver.find_element_by_id("check1").click()
time.sleep(4)
driver.close()