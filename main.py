import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys





if __name__ == '__main__':
    my_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=my_options)
    browser.get('https://web.whatsapp.com')

    time.sleep(50)

    name_list = ['Ma','Baba','Trisha']
    text = 'hello there'

    for name in name_list:


        # finding a name using search
        chat_new = browser.find_element(By.XPATH, value='//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    
        chat_new.click()
        chat_new.send_keys(name)
        chat_new.send_keys(Keys.RETURN)


        # try:
        #     user = browser.find_element(By.XPATH, value='//*[@id="main"]/header/div[2]/div/div[1]')
        #     user.click()

        # except Exception as e:
        #     print(e)
        

        box_message = browser.find_element(By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
        
        box_message.send_keys(text)
        time.sleep(10)
        box_message = browser.find_element(By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]')
        box_message.click()

        time.sleep(20)

    
    browser.close()
