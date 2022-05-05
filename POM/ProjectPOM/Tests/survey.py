from selenium import webdriver
import time
import unittest
from selenium.webdriver.chrome.service import Service

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

from POM.ProjectPOM.Pages.loginPage import LoginPage
from POM.ProjectPOM.Pages.homePage import HomePage
from POM.ProjectPOM.Pages.surveyPage import SurveyPage
from POM.ProjectPOM.Pages.librarySurvey import LibrarySurvey


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service("E:\Software_Test\POM_NgoBaoCong_47896\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_survey(self):
        driver = self.driver

        driver.get("http://my.uda.edu.vn/sv/svlogin")
        login = LoginPage(driver)
        login.enter_username("47896")
        login.enter_password("123456")
        login.click_login()
        print("----------------------------------")
        print("Đăng nhập thành công!")
        print("----------------------------------")

        homepage = HomePage(driver)
        homepage.click_info_class()
        homepage.click_survey_answer()
        print("----------------------------------")
        print("Đã vào trang khảo sát!")
        print("----------------------------------")

        surveypage = SurveyPage(driver)
        surveypage.click_about_library()

        librarypage = LibrarySurvey(driver)
        librarypage.click_library_0()
        librarypage.click_library_1()
        librarypage.click_library_2()
        librarypage.click_library_3_0()
        librarypage.click_library_3_1()
        librarypage.click_library_4_2()
        librarypage.click_library_4_3()
        librarypage.click_library_5()
        librarypage.click_library_7()
        librarypage.click_library_8()
        librarypage.click_library_9()
        librarypage.click_library_10()
        librarypage.click_library_11()
        librarypage.click_library_12()
        librarypage.click_library_13()
        librarypage.click_library_14()
        librarypage.click_library_15()
        librarypage.click_library_16()
        librarypage.click_library_17()
        librarypage.click_library_19()
        librarypage.click_library_20()
        librarypage.click_library_21()
        librarypage.click_library_22()
        librarypage.click_library_23()
        librarypage.click_library_24()
        librarypage.click_library_25()
        librarypage.click_library_26()
        librarypage.click_library_27()
        librarypage.click_library_28()
        librarypage.click_library_29()
        librarypage.click_library_30()
        librarypage.click_library_31()
        librarypage.click_library_32()
        librarypage.click_library_33()
        librarypage.click_library_34()
        librarypage.click_library_35()

        librarypage.enter_cmt_1("Thư viện rất thoáng mát và có nhạc nhẹ")
        librarypage.enter_cmt_2("Chưa có")
        librarypage.enter_cmt_3("Chưa có")

        # librarypage.click_survey_save()

        print("----------------------------------")
        print("Đã lưu khảo sát!")
        print("----------------------------------")
        print("----------------------------------")
        print("Hoàn thành khảo sát!")
        print("----------------------------------")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Hoàn thành kiểm thử!')


if __name__ == '__main__':
    unittest.main()
