from selenium.webdriver.common.by import By

from POM.ProjectPOM.Locators.location import Locators

class SurveyPage():

    def __init__(self, driver):
        self.driver = driver

        self.about_library = Locators.about_library


    def click_about_library(self):
        self.driver.find_element(By.LINK_TEXT, self.about_library).click()


