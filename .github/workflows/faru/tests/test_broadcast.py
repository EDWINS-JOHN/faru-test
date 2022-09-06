from asyncio.log import logger
import email
from locale import currency
import pytest
import time
import string
import random
from pom.LoginPage import LoginPage
from pom.Create_Broadcast import Crate_Broadcast
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
import datetime


class Test_broadcast:
     baseurl = ReadConfig.getAppURL()
     email = ReadConfig.get_email()
     password = ReadConfig.get_password()
     number = "2"
     origin = "Nairobi"
     destination = "Kampala"
     trucks_no = "2"
     commodity = "Fertilizer"
     amount_price = "2000"
     amount = "USD"
    
     logger = LogGen.loggen()
     


     def test_create_broadcast(self,setup):
          self.logger.info("********* Start of create_broadcast test *******")
          self.driver=setup
          self.driver.get(self.baseurl)
          
          self.login=LoginPage(self.driver)
          self.login.get_email(self.email)
          self.login.get_password(self.password)
          self.login.click_login()
          self.logger.info("********* login successful *******")

          self.logger.info("********* create_broadcast test *******")
          time.sleep(5)
          
          self.create_broadcast = Crate_Broadcast(self.driver)
          self.create_broadcast.click_broadcast()
          self.driver.implicitly_wait(10)
          self.create_broadcast.click_create()
          self.create_broadcast.number_of_broadcast(self.number)
          self.create_broadcast.next_btn_create_broadcast()
          self.driver.implicitly_wait(10)
          self.orderID =  random.randint(10000,20000)
          self.create_broadcast.order_id(self.orderID)
          # date = datetime.datetime.now()
          # dat= date.strftime("%y%d%m")
          # print (dat)
          # self.create_broadcast.loading_window_start(dat)

          self.driver.implicitly_wait(10)
          self.create_broadcast.origin(self.origin)
          self.create_broadcast.number_of_trucks(self.trucks_no)
          self.create_broadcast.amount_currency(self.amount)
          self.driver.implicitly_wait(10)
          # self.create_broadcast.amount_type()
          # self.create_broadcast.truck_type()
          # self.create_broadcast.loading_window_end()
          self.create_broadcast.destination(self.destination)
          self.create_broadcast.commodity(self.commodity)
          self.create_broadcast.amount(self.amount_price)
          self.create_broadcast.finish_btn()
          time.sleep(10)
          self.driver.close()






