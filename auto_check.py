from concurrent.futures import BrokenExecutor
from multiprocessing.sharedctypes import Value
from tokenize import Name
from xml.dom.minidom import Document, Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
import time
import os
def getInfo(targetKey):
    os.system("taskkill /F /im chromedriver.exe")
    os.system("taskkill /F /im chrome.exe")
    option = webdriver.ChromeOptions()
    user_data_dir=r"C:\Users\Zheng'bo'yang\AppData\Local\Google\Chrome\User Data" 
    option.add_argument(f'--user-data-dir={user_data_dir}')
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=option)
    browser.get(r"https://form.sjtu.edu.cn/infoplus/form/12356324/render")
    time.sleep(1.5)
    #Finance=browser.find_elements_by_xpath("//*[@id='app']/div/div[1]/div[1]/div/div[2]/div/div[1]/div[4]/div[1]/p[1]")
    #Finance.click()
    print("List Got")
    browser.implicitly_wait(5)
    target=browser.find_element(by=By.XPATH,value=r"//*[@id='V0_CTRL4']/option[3]")
    target.click()
    browser.implicitly_wait(5)
    targetWindow=browser.find_elements(by=By.XPATH,value=r"//input")[4]
    targetWindow.send_keys(targetKey)
    time.sleep(1.5)
    targetWindow.send_keys(Keys.ENTER)
    time.sleep(1)
    try:
        Name=browser.find_element(by=By.XPATH,value=r'//*[@id="V0_CTRL15_0"]/*')
        print("姓名:",' ')
        print(Name.get_attribute('text'))
    except:
        print("No Such User or Unknown Error")
    '''
    table=browser.find_elements(by=By.ID,value=r'//*[@class="suggest_unselected infoplus_suggester_item"]')
    for i in table:
        print(i)
    '''
    try:
        #js='Document.getElementById("V0_CTRL17_0")'
        #browser.execute_script(js)
        JA=browser.find_elements(by=By.XPATH,value=r'//div[@class="infoplus_control infoplus_labelControl"]')[1]
        print("Jaccount:",' ')
        print(JA.text)
    except:
        print("No Such User or Unknown Error")
    try:
        School=browser.find_elements(by=By.XPATH,value=r'//div[@class="infoplus_control infoplus_labelControl"]')[2]
        print("学院:",' ')
        print(School.text)
    except:
        print("No Such User or Unknown Error")
    #time.sleep(10)
    browser.close()
if __name__=='__main__':
    targetKey=input("学号\工号\姓名\姓名拼音\Jaccount:")
    getInfo(targetKey)