from selenium import webdriver  
from time import sleep

def login():
    global driver
    driver = webdriver.Firefox(executable_path='geckodriver.exe')  
    driver.maximize_window()
    driver.get('https://www.matchbook.com/')
    driver.add_cookie({"name": "mb-client-type", "value": "mb-web-ui"})
    driver.implicitly_wait(20) 
    return driver

def click():
    driver.find_element('xpath', '//div[@class="NavSubMenu__menuLink___JVOuL"]/a').click()
    sleep(3)
    
if __name__ == '__main__':
    login()