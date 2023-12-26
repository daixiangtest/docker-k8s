import time

from selenium import webdriver

# 远程Docker服务的地址和端口
# wd 表示 WebDriver，hub 表示服务器的入口点。
# 通过在 URL 中指定 /wd/hub，您告诉 Selenium 客户端要连接到远程的 WebDriver 服务器
# 服务器4444映射到docker中4444端口也就是Webdriver-selenim服务端口
# realvnc5900 端口用来查看容器类浏览器的图形化界面


remote_url = 'http://192.168.22.238:4444'

# 配置浏览器选项
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 连接到远程Selenium Chrome节点
driver = webdriver.Remote(command_executor=remote_url, options=chrome_options)
# driver=webdriver.Chrome()
# 打开浏览器
driver.get('https://www.baidu.com')
print(1)
driver.maximize_window()
print(2)
a = driver.title
print(a)
print(1)
time.sleep(10)
driver.quit()
