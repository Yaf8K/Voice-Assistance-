from selenium import webdriver
import pyttsx3 as p


# Class to see Information

class Movie():
    def __init__(self):
        self.driver = webdriver.Safari(executable_path='/usr/bin/safariing)')

    def ReviewMovie(self, name):
        self.driver.get(url="https://www.wikipedia.org/")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(name + "movie reviews") # name of the movies will pass as a parameter

        submit = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        submit.click()

        bot = Movie()
        bot.ReviewMovie("Life of PI")
