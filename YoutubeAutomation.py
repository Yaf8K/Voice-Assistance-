#class to play a music video on youtube
from selenium import webdriver
class PlayMusic():
    def __init__(self):
        self.driver = webdriver.Safaree()

    def play(self,name):
        self.name = name
        #Using the url from youtube.com
        #Using the url Ill be getting the query.

        self.driver.get(url = "https://www.youtube.com/results?search_query=" + name)# Search query
        video = self.driver.find_element_by_xpath('//*[@id = "dismissable"]') #It will be using the designated x path after loading the website to play the video.
        video.click()

        # I will be calling the music AUTOMATION CLASS
        bot = PlayMusic()
        bot.play("Minato Shipudden")

