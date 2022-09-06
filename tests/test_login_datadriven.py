import pytest
from selenium import webdriver
from pom.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import xlutils
import time


class Test_002_Login_datadriven:

    baseurl = ReadConfig.getAppURL()
    path = "/home/mamba-cita/test/faru/TestData/LoginData1.xlsx" 
    logger = LogGen.loggen()

    def test_login_datadriven(self, setup):
        self.logger.info(
            "******************** Test_login_datadriven ************")
        self.logger.info(
            "******************** Started login test ************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.login = LoginPage(self.driver)

        self.rows = xlutils.getColumnCount(self.path, 'sheet1')
        print("Number of Rows i a Excel:", self.rows)

        list_status = []

        for r in range(2, self.rows+1):
            self.email = xlutils.readData(self.path, 'sheet2', r, 1)
            self.password = xlutils.readData(self.path, 'sheet2', r, 2)
            self.exp = xlutils.readData(self.path, 'sheet2', r, 3)

            self.login.get_email(self.email)
            self.login.get_password(self.password)
            self.login.click_login()
            time.sleep(5)

            actual_title = self.driver.title
            exp_title = "Faru"

            if actual_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**** test Passed ")
                    self.login.user_Profile()
                    self.login.click_logout()
                    list_status.append("Passed")
                elif self.exp == "Fail":
                    self.logger.info("**** test Failed ")
                    self.login.user_Profile()
                    self.login.click_logout()
                    list_status.append("Failed")
            elif actual_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("**** test Failed ")
                    list_status.append("Failed")
                elif self.exp == "Fail":
                    self.logger.info("**** test Passed ")
                    list_status.append("Passed")

        if "Fail" not in list_status:
                self.logger.info("**** test passed ***** ")
                self.driver.close()
                assert True
        else:
                self.logger.info("**** test Failed ***** ")
                self.driver.close()
                assert False
          
        self.logger.info(" ******** End of Login Test *****")
        self.logger.info("****** Completed ********")