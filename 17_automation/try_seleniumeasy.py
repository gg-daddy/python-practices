from selenium import webdriver
from selenium.webdriver.common.by import By

# https://sites.google.com/chromium.org/driver/getting-started?authuser=0
# 已经把 chromedriver 放到了 path 路径下，所以下面无需指定参数。
chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window()
chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

# 在输入框中输入内容
user_message_input = chrome_browser.find_element(
    by=By.ID, value="user-message")
input_text = "Hello World!"
user_message_input.send_keys(input_text)

# 点击按钮
btn = chrome_browser.find_element(by=By.CLASS_NAME, value="btn-primary")
btn.click()

# 检查显示的文本是否和输入的文本一致
display_text = chrome_browser.find_element(by=By.ID, value="display").text
assert display_text == input_text

# 可以使用 https://www.selenium.dev/selenium-ide/ 来录制操作，然后转换成代码。

# Selenium可以通过一个名为Appium的扩展来支持Android和iOS应用的自动化测试。
# Appium是一个开源的自动化测试框架，它使用WebDriver协议来驱动iOS和Android应用。
# 你可以使用Selenium的API来编写测试，然后通过Appium来运行这些测试。
