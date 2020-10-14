# Selenium
紀錄如何使用Selenium  
import selenium
from selenium import webdriver  
driver = webdriver.Firefox()  

driver.find_element_by_xpath()

# Keys  
from selenium.webdriver.common.keys import Keys
Enter Keys.ENTER  
刪除鍵 Keys.BACK_SPACE  
空格鍵 Keys.SPACE  
制表鍵 Keys.TAB  
回退鍵 Keys.ESCAPE  
刷新鍵 Keys.F5  
全選（Ctrl+A）(Keys.CONTROL,'a')  
復制（Ctrl+C）(Keys.CONTROL,'c')  
剪切（Ctrl+X）(Keys.CONTROL,'x')  
粘貼（Ctrl+V）(Keys.CONTROL,'v')  


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

# 下拉至底  
driver.execute_script("window.scrollTo(0, 1000)")

# Selenium  
https://medium.com/@yanweiliu/python%E7%88%AC%E8%9F%B2%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E4%BA%8C-selenium%E8%87%AA%E5%8B%95%E5%8C%96-ab0a27a94ff2  

# Timeout  
driver.set_page_load_timeout(second)  
