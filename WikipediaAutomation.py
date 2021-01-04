from selenium import webdriver
import pyttsx3 as p
from webdriver_manager.chrome import ChromeDriverManager




#Class used to see the information

class Information():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) # executable path where chrome is

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org/")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()
        
        #The definition of the bot can read
        Information = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/p[2]')
        readable_text = Information.text #
        engine = p.init()
        engine.say(readable_text)# after it fetches the data to is going to say the info
        engine.runAndWait()

        bot = Information()
        bot.get_info("Concord University")
