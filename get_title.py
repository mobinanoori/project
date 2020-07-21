from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.implicitly_wait(15)
driver.maximize_window()

driver.get("http://www.google.com")

print(driver.title ) 

search_field = driver.find_element_by_id("id")
search_field.clear()

search_field.send_keys("Selenium WebDriver")
search_field.submit()

lists= driver.find_elements_by_class_name("_Rm")

print ("Found " + str(len(lists)) + " searches:")

i=0
for listitem in lists:
   print (listitem.get_attribute("innerHTML"))
   i=i+1
   if(i>10):
      break

driver.quit()