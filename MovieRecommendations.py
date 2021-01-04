
class Recommendation():
    def __init__(self):
        self.driver = webdriver.Safaree(executable_path = '/usr/bin/safariing)' )


    def Recommendation_Info(self):
        self.driver.get(url = " https://www.imdb.com/chart/moviemeter/?ref_n_mv_mpm")# Its going to take to the imdp list of movies  recommendation and display most popular path.
        select = self.driver.find_element_by_xpath('//*[@id = "lister-sort-by-options"]')
        select.click()

    #bot = Recommendation()
    #bot.Recommendation_Info()