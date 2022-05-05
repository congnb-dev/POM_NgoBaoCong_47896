from selenium.webdriver.common.by import By

from POM.ProjectPOM.Locators.location import Locators


class AccPage():

    def __init__(self, driver):
        self.driver = driver

        self.owner_name = Locators.owner_name
        self.owner_tel = Locators.owner_tel
        self.owner_rela = Locators.owner_rela
        self.motel_number = Locators.motel_number
        self.street = Locators.street
        self.resid = Locators.resid
        self.dictrict = Locators.dictrict
        self.town = Locators.town
        self.leader_name = Locators.leader_name
        self.leader_tel = Locators.leader_tel
        self.acc_save = Locators.acc_save
        self.acc_delete = Locators.acc_delete
        self.acc_confirm = Locators.acc_confirm

    def enter_owner_name(self, owner_name):
        self.driver.find_element(By.ID, self.owner_name).send_keys(owner_name)

    def enter_owner_tel(self, owner_tel):
        self.driver.find_element(By.ID, self.owner_tel).send_keys(owner_tel)

    def enter_owner_rela(self, owner_rela):
        self.driver.find_element(By.ID, self.owner_rela).send_keys(owner_rela)

    def enter_motel_number(self, motel_number):
        self.driver.find_element(By.ID, self.motel_number).send_keys(motel_number)

    def enter_street(self, street):
        self.driver.find_element(By.ID, self.street).send_keys(street)

    def enter_resid(self, resid):
        self.driver.find_element(By.ID, self.resid).send_keys(resid)

    def select_dictrict(self):
        self.driver.find_element(By.ID, self.dictrict).click()

    def select_town(self):
        self.driver.find_element(By.ID, self.town).click()

    def enter_leader_name(self, leader_name):
        self.driver.find_element(By.ID, self.leader_name).send_keys(leader_name)

    def enter_leader_tel(self, leader_tel):
        self.driver.find_element(By.ID, self.leader_tel).send_keys(leader_tel)

    def click_acc_save(self):
        self.driver.find_element(By.ID, self.acc_save).click()

    def click_acc_delete(self):
        self.driver.find_element(By.ID, self.acc_delete).click()

    def click_acc_confirm(self):
        self.driver.find_element(By.ID, self.acc_confirm).click()