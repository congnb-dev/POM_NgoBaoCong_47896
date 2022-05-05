from selenium.webdriver.common.by import By

from POM.ProjectPOM.Locators.location import Locators


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.infor_class = Locators.infor_class
        self.survey_answer = Locators.survey_answer
        self.accommodation = Locators.accommodation
        self.add = Locators.add

    def click_info_class(self):
        self.driver.find_element(By.LINK_TEXT, self.infor_class).click()

    def click_survey_answer(self):
        self.driver.find_element(By.LINK_TEXT, self.survey_answer).click()

    def click_accommodation(self):
        self.driver.find_element(By.LINK_TEXT, self.accommodation).click()

    def click_add(self):
        self.driver.find_element(By.ID, self.add).click()
