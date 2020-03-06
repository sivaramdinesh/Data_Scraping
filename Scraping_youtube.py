from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd



driver = webdriver.Firefox()
driver.get(r"https://www.youtube.com/results?search_query=janasena&sp=EgIQAQ%253D%253D")

user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
links=[]
for i in user_data:
    links.append(i.get_attribute('href'))

df=pd.DataFrame(links)


print(df)
driver.close()    
