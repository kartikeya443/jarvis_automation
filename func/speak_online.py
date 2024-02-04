#pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.headless = True

driver = webdriver.Chrome(options=chrome_options)
website = r"https://ttsmp3.com/text-to-speech/British2English/"
driver.get(website)

#copy voice id from inspect element for that webpage
button_selection = Select(driver.find_element(by=By.ID, value='sprachwahl'))
button_selection.select_by_visible_text("British English / Brian")

def Speak(*args):
    
    text = ""
    for i in args:
        text += i
    length_oftext = len(str(text))
    if length_oftext == 0:
        pass
    else:
        print("")
        print(f"JARVIS: {text}.")
        print("")
        data = str(text)
        
        #copy id of text area from inspect element
        driver.find_element(By.ID, "voicetext").send_keys(data)
        driver.find_element(By.ID, value="vorlesenbutton").click()
        driver.find_element(By.ID, "voicetext").clear()
        
        if length_oftext >= 30:
            sleep(7)
        elif length_oftext >= 40:
            sleep(8)
        elif length_oftext >= 55:
            sleep(12)
        elif length_oftext >= 70:
            sleep(14)
        elif length_oftext >= 108:
            sleep(16)
        elif length_oftext >= 128:
            sleep(18)
        else:
            sleep(2)

#Speak("hi my name is kartikeya acharya")