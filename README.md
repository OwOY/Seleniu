# Selenium
紀錄如何使用Selenium  
import selenium
# Driver Firefox
from selenium import webdriver  
driver = webdriver.Firefox()  

# Driver Firefox Profile

profile = webdriver.FirefoxProfile()  
profile.set_preference('browser.download.dir', path)  設定路徑  
profile.set_preference('browser.download.folderList', 2)  1為預設路徑   2為自訂路徑  
profile.set_preference('browser.download.manager.showWhenStarting', False)  是否顯示下載管理器
driver = webdriver.Firefox(firefox_profile=profile)

# ActionChains 模仿滑鼠操作

from selenium.webdriver.common.action_chains import ActionChains  
action = ActionChains(driver).move_to_element(element)  移動到元素位置  
action.context_click().perform()  操作右鍵選單  


