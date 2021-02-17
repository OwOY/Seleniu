import selenium
from selenium import webdriver  
from time import sleep
from password import pswd1

class Dcard:

    def __init__(self):

        self.driver = webdriver.Firefox(executable_path='/home/test/Documents/git/Selenium/geckodriver')  
        self.account = pswd1()['account']
        self.password = pswd1()['password']


    # def main(self):
        
    #     self.login()
    #     self.post()


    def login(self):
        
        self.driver.get('https://www.dcard.tw/signup')
        sleep(2)
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(f'{self.account}')  
        sleep(1)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(f'{self.password}')
        sleep(1)
        self.driver.find_element_by_xpath('//button[@type="submit" and contains(text(),"登入")]').click()
    #     # driver.close()

    def post(self):
        
        board_name = "天竺鼠車車"
        self.driver.find_element_by_xpath('//button[contains(.//text(),"發表")]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//div[contains(./text(),"選擇")]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//input[@placeholder="尋找看板"]').send_keys(board_name)
        sleep(1)
        self.driver.find_element_by_xpath(f'//div[contains(./text(),"{board_name}")]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//textarea[@name="title"]').send_keys('test')
        sleep(1)
        self.driver.find_element_by_xpath('//div[@roll="textbox"]').send_keys('test')
        sleep(1)
        self.driver.find_element_by_xpath('//div[contains(text(),"選擇發文身份")]').send_keys('test')
        

if __name__ == '__main__':

    Dcard().post()
