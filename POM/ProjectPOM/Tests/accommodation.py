from selenium import webdriver
import time
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

from POM.ProjectPOM.Pages.loginPage import LoginPage
from POM.ProjectPOM.Pages.homePage import HomePage
from POM.ProjectPOM.Pages.accommodationPage import AccPage



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
        driver.save_screenshot("E:/Software_Test/POM_NgoBaoCong_47896/POM/ProjectPOM/reports/login_done.png")

        homepage = HomePage(driver)
        homepage.click_info_class()
        homepage.click_accommodation()
        print("----------------------------------")
        print("Đã vào trang Thông tin ngoại trú!")
        print("----------------------------------")
        homepage.click_add()

        acc = AccPage(driver)
        acc.enter_owner_name("Phoan Hiển")
        acc.enter_owner_tel("0905123456")
        acc.enter_owner_rela("Cha con")
        acc.enter_motel_number("32")
        acc.enter_street("Tiên Sơn 19")
        acc.enter_resid("68")
        selectDict = Select(driver.find_element(By.ID,"MainContent_D2"))
        selectDict.select_by_value('1')
        selectDict = Select(driver.find_element(By.ID, "MainContent_D3"))
        selectDict.select_by_value('25')
        acc.enter_leader_name("Nguyễn Văn Nhật")
        acc.enter_leader_tel("0905987654")
        driver.save_screenshot("E:/Software_Test/POM_NgoBaoCong_47896/POM/ProjectPOM/reports/acc_shot_done.png")
        acc.click_acc_save()
        print("----------------------------------")
        print("Đã lưu Thông tin ngoại trú!")
        print("----------------------------------")
        acc.click_acc_delete()
        acc.click_acc_confirm()
        print("----------------------------------")
        print("Đã xóa Thông tin ngoại trú!")
        print("----------------------------------")


        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Hoàn thành kiểm thử!')


if __name__ == '__main__':
    unittest.main()
