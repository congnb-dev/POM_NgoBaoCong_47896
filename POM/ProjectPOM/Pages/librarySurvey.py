from selenium.webdriver.common.by import By

from POM.ProjectPOM.Locators.location import Locators

class LibrarySurvey():

    def __init__(self, driver):
        self.driver = driver

        self.library_0 = Locators.library_0
        self.library_1 = Locators.library_1
        self.library_2 = Locators.library_2
        self.library_3_0 = Locators.library_3_0
        self.library_3_1 = Locators.library_3_1
        self.library_4_3 = Locators.library_4_3
        self.library_4_2 = Locators.library_4_2
        self.library_5 = Locators.library_5
        self.library_7 = Locators.library_7
        self.library_8 = Locators.library_8
        self.library_9 = Locators.library_9
        self.library_10 = Locators.library_10
        self.library_11 = Locators.library_11
        self.library_12 = Locators.library_12
        self.library_13 = Locators.library_13
        self.library_14 = Locators.library_14
        self.library_15 = Locators.library_15
        self.library_16 = Locators.library_16
        self.library_17 = Locators.library_17
        self.library_19 = Locators.library_19
        self.library_20 = Locators.library_20
        self.library_21 = Locators.library_21
        self.library_22 = Locators.library_22
        self.library_23 = Locators.library_23
        self.library_24 = Locators.library_24
        self.library_25 = Locators.library_25
        self.library_26 = Locators.library_26
        self.library_27 = Locators.library_27
        self.library_28 = Locators.library_28
        self.library_29 = Locators.library_29
        self.library_30 = Locators.library_30
        self.library_31 = Locators.library_31
        self.library_32 = Locators.library_32
        self.library_33 = Locators.library_33
        self.library_34 = Locators.library_34
        self.library_35 = Locators.library_35

        self.library_cmt_1 = Locators.library_cmt_1
        self.library_cmt_2 = Locators.library_cmt_2
        self.library_cmt_3 = Locators.library_cmt_3

        self.library_save = Locators.library_save


    def click_library_0(self):
        self.driver.find_element(By.ID, self.library_0).click()

    def click_library_1(self):
        self.driver.find_element(By.ID, self.library_1).click()


    def click_library_2(self):
        self.driver.find_element(By.ID, self.library_2).click()

    def click_library_3_0(self):
        self.driver.find_element(By.ID, self.library_3_0).click()

    def click_library_3_1(self):
        self.driver.find_element(By.ID, self.library_3_1).click()

    def click_library_4_3(self):
        self.driver.find_element(By.ID, self.library_4_3).click()

    def click_library_4_2(self):
        self.driver.find_element(By.ID, self.library_4_2).click()

    def click_library_5(self):
        self.driver.find_element(By.ID, self.library_5).click()

    def click_library_7(self):
        self.driver.find_element(By.ID, self.library_7).click()

    def click_library_8(self):
        self.driver.find_element(By.ID, self.library_8).click()

    def click_library_9(self):
        self.driver.find_element(By.ID, self.library_9).click()

    def click_library_10(self):
        self.driver.find_element(By.ID, self.library_10).click()

    def click_library_11(self):
        self.driver.find_element(By.ID, self.library_11).click()

    def click_library_12(self):
        self.driver.find_element(By.ID, self.library_12).click()

    def click_library_13(self):
        self.driver.find_element(By.ID, self.library_13).click()

    def click_library_14(self):
        self.driver.find_element(By.ID, self.library_14).click()

    def click_library_15(self):
        self.driver.find_element(By.ID, self.library_15).click()

    def click_library_16(self):
        self.driver.find_element(By.ID, self.library_16).click()

    def click_library_17(self):
        self.driver.find_element(By.ID, self.library_17).click()

    def click_library_19(self):
        self.driver.find_element(By.ID, self.library_19).click()

    def click_library_20(self):
        self.driver.find_element(By.ID, self.library_20).click()

    def click_library_21(self):
        self.driver.find_element(By.ID, self.library_21).click()

    def click_library_22(self):
        self.driver.find_element(By.ID, self.library_22).click()

    def click_library_23(self):
        self.driver.find_element(By.ID, self.library_23).click()

    def click_library_24(self):
        self.driver.find_element(By.ID, self.library_24).click()

    def click_library_25(self):
        self.driver.find_element(By.ID, self.library_25).click()

    def click_library_26(self):
        self.driver.find_element(By.ID, self.library_26).click()

    def click_library_27(self):
        self.driver.find_element(By.ID, self.library_27).click()

    def click_library_28(self):
        self.driver.find_element(By.ID, self.library_28).click()

    def click_library_29(self):
        self.driver.find_element(By.ID, self.library_29).click()

    def click_library_30(self):
        self.driver.find_element(By.ID, self.library_30).click()

    def click_library_31(self):
        self.driver.find_element(By.ID, self.library_31).click()

    def click_library_32(self):
        self.driver.find_element(By.ID, self.library_32).click()

    def click_library_33(self):
        self.driver.find_element(By.ID, self.library_33).click()

    def click_library_34(self):
        self.driver.find_element(By.ID, self.library_34).click()

    def click_library_35(self):
        self.driver.find_element(By.ID, self.library_35).click()

    def enter_cmt_1(self,cmt1):
        self.driver.find_element(By.ID, self.library_cmt_1).send_keys(cmt1)

    def enter_cmt_2(self,cmt2):
        self.driver.find_element(By.ID, self.library_cmt_2).send_keys(cmt2)

    def enter_cmt_3(self,cmt3):
        self.driver.find_element(By.ID, self.library_cmt_3).send_keys(cmt3)


    def click_survey_save(self):
        self.driver.find_element(By.ID, self.library_save).click()

