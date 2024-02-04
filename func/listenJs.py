#pip intall selenium

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)
website = r"C:\Users\karti\Desktop\py_projects\jarvis_automation\data\voice.html"

driver.get(website)

def Listen():
    print("Listening...")
    driver.find_element(by=By.ID, value='start').click()
    
    while 1:
        text = driver.find_element(by=By.ID, value='output').text
        if text != "":
            print("You said: " + text)
            driver.find_element(by=By.ID, value='end').click()
            return text

while 1:
    Listen()