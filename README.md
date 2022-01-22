<p align='center'>
  <img height=250px width=550px src='https://learningactors.com/wp-content/uploads/2017/06/selenium.png'/>
</p>

## How to use Selenium
```
import selenium
from selenium import webdriver  
driver = webdriver.Firefox(executable_path=<your driver path>)  
driver.get({url})
driver.find_element_by_xpath()  
driver.close()
```
取得網址 : driver.current_url  

## Web狀態  
driver.set_window_size(480,800)  
driver.maximize_window()  #視窗最大化  
driver.back()       #上一頁  
driver.forward()    #下一頁  
driver.refresh()    #重整  
driver.get_screenshot_as_file("xxx.jpg")    #視窗截圖  

## Options Setting 
```
from selenium.webdriver.firefox.options import Options  
options = Options()  
options.headless = True  
```

## 獲取定位元素值    

i = driver.find_element_by_xpath("")   
i.get_attribute("data-id")  #取得元素值  
i.text     #顯示元素文字    
i.size     #顯示元素尺寸  
i.click() #點擊  
i.submit() #提交表單  


## Keys  
```
from selenium.webdriver.common.keys import Keys
driver.find_element_by_xpath().send_keys({text})    
```
- Enter 
```
Keys.ENTER  
```
- 刪除鍵 
```
Keys.BACK_SPACE  
```
- 空格鍵 
```
Keys.SPACE  
```
- 制表鍵 
```
Keys.TAB  
```
- 回退鍵 
```
Keys.ESCAPE  
```
- 刷新鍵 
```
Keys.F5  
```
- 全選（Ctrl+A）
```
(Keys.CONTROL,'a')
```
- 復制（Ctrl+C）
```
(Keys.CONTROL,'c') 
```
- 剪切（Ctrl+X）
```
(Keys.CONTROL,'x')  
```
- 粘貼（Ctrl+V）
```
(Keys.CONTROL,'v')  
```
## Driver Chrome
- 關閉通知
```
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
        }
}
driver = webdriver.Chrome(service=xxx, options=options)

```
## Driver Firefox Profile

https://medium.com/@yanweiliu/python%E7%88%AC%E8%9F%B2%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E4%BA%8C-selenium%E8%87%AA%E5%8B%95%E5%8C%96-ab0a27a94ff2  

```
profile = webdriver.FirefoxProfile()  
profile.set_preference('browser.download.dir', path)  設定路徑  
profile.set_preference('browser.download.folderList', 2)  1為預設路徑   2為自訂路徑  
profile.set_preference('browser.download.manager.showWhenStarting', False)  是否顯示下載管理器
driver = webdriver.Firefox(firefox_profile=profile)
```

## 偽裝手機
```
mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}  
options = webdriver.ChromeOptions()  
options.add_experimental_option('mobileEmulation', mobileEmulation)  
driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
```

## ActionChains 模仿滑鼠操作
```
from selenium.webdriver.common.action_chains import ActionChains  
action = ActionChains(driver).move_to_element(element)  移動到元素位置  
action.context_click().perform()  操作右鍵選單  
```

## JS拉桿下拉  
```
driver.execute_script("window.scrollTo(0, 1000)")
```

## Timeout  
```
driver.set_page_load_timeout(second)  
```

## Selenium 網頁Handle

上一頁: driver.back()  
下一頁: driver.forward()  
刷新:driver.refresh()  
取得當前網址:driver.current_url  
取得當前分頁:driver.title  
當前視窗:driver.current_window_handle  
所有視窗:driver.window_handles  
視窗切換:driver.switch_to.window(<window_handle>)

# ==========隱藏Selenium操作==========  
https://juejin.im/post/6844904095749242887


