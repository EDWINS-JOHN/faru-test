
from asyncio.log import logger
import pytest
from selenium import webdriver
from pom.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    baseurl = ReadConfig.getAppURL()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()


    logger=LogGen.loggen()



    def test_login_title(self, setup):
        self.logger.info("******************** Test_01_Login ************")
        self.logger.info("******************** Started verifying landing_page title ************")
        self.driver = setup
        self.driver.get(self.baseurl)
        actual_title = self.driver.title
        if actual_title == "Faru":
            assert True
            self.driver.close()
            self.logger.info("******************** landing page title test Passed ************")
        else:
            self.driver.save_screenshot("../Screenshots/"+"landing_page_title.png")
            self.driver.close()
            self.logger.error("******************** landing page title test Failed ************")
            assert False

    def test_login(self, setup):
        self.logger.info("******************** Test_login ************")
        self.logger.info("******************** Started login test ************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.login = LoginPage(self.driver)
        self.login.get_email(self.email)
        self.login.get_password(self.password)
        self.login.click_login()
        actual_title = self.driver.title

        if actual_title == "Faru":
            assert True
            self.driver.close()
            self.logger.info("******************** login test passed ************")
        else:
            self.driver.save_screenshot("../Screenshots/"+"login_title.png")
            self.driver.close()
            self.logger.info("******************** login test Failed ************")
            assert False
