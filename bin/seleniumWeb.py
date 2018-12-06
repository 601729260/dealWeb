from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://pos3.mamhao.com/login?host=1")


print(driver.title)
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[1]/div[2]/form/div[1]/div/div/input").send_keys("wgnfd")
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[1]/div[2]/form/div[2]/div/div/input").send_keys("123456")

driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[1]/div[2]/form/div[3]/div/div/div/input").click()
ActionChains(driver).move_by_offset(100,100)



#driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[1]/div[2]/form/div[4]/div/div/input").send_keys("http://192.168.50.198:8018")


#time.sleep(3)
#driver.close()