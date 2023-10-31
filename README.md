<p align='center'>
  <img height=250px width=550px src='https://learningactors.com/wp-content/uploads/2017/06/selenium.png'/>
</p>

## How to use Selenium
1. Create web driver
    - Firefox  
      ```
      from selenium import webdriver  
      driver = webdriver.Firefox()  
      ```
    - Chrome  
      ```
      from selenium
      driver = webdriver.Chrome()
      ```
    #### 若出現 'chromedriver' executable needs to be in PATH 之情況，可配合套件使用  
    - install 
      ```
      python -m pip install webdriver_manager
      ```
    - use
      ```
      from webdriver_manager.chrome import ChromeDriverManager


      driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
      ```

## Options Setting 
```
from selenium.webdriver.firefox.options import Options  
options = Options()  
options.headless = True  # 無痕

prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
        }
}
options.add_experimental_option('prefs', prefs) # 關閉瀏覽器彈窗通知
options.add_experimental_option('detach', True) # 不自動關閉瀏覽器
```
## 連結已開啟之瀏覽器
1. 設置參數開啟瀏覽器  
    ```
    chrome.exe --remote-debugging-port=9222 --user-data-dir="E:\selenium"
    ```
2. 使用option設定連結瀏覽器  
    ```
    chrome_option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    ```

## driver setting
- 設定視窗大小
  ```
  driver.set_window_size(480,800)
  ```
- 視窗最大化
  ```
  driver.maximize_window()
  ```
- 上一頁
  ```
  driver.back()
  ```
- 下一頁  
  ```
  driver.forward()
  ```
- 刷新頁面
  ```
  driver.refresh()
  ```
- 視窗截圖  
  ```
  driver.get_screenshot_as_file("xxx.jpg")
  ```
- 取得網址
  ```
  driver.current_url
  ```
- 取得取得當前標題
  ```
  driver.title  
  ```
- 切換iframe
  ```
  driver.switch_to.frame(0)
  ```
- 上一頁
  ```
  driver.back()  
  ```
- 下一頁
  ```
  driver.forward()  
  ```
- 取得當前視窗
  ```
  driver.current_window_handle
  ```
- 取得所有視窗
  ```
  driver.window_handles 
  ```
- 視窗切換
  ```
  driver.switch_to.window(<window_handle>)
  ```

## 獲取定位元素值    
- 取得元素
  ```
  ele = driver.find_element('xpath', '')   
  ```
- 取得屬性值   
  ```
  ele.get_attribute("data-id")   
  ```
- 顯示元素文字 
  ```
  ele.text
  ```
- 顯示元素尺寸  
  ```
  ele.size 
  ```
- 點擊
  ```
  ele.click() 
  ```
- 提交表單  
  ```
  ele.submit()
  ```
- 傳送訊息
  ```
  ele.send_keys(text)
  ```
  ### text內容
  - 文字
    ```
    abc
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

## Driver Firefox Profile
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

## 隱藏Selenium操作  
[如何正确移除Selenium中的 window.navigator.webdriver](https://juejin.im/post/6844904095749242887)


## 參考資料
[Python爬蟲筆記](https://medium.com/@yanweiliu/python%E7%88%AC%E8%9F%B2%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E4%BA%8C-selenium%E8%87%AA%E5%8B%95%E5%8C%96-ab0a27a94ff2)