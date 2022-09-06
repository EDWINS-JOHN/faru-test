from datetime import datetime
from select import select
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class Crate_Broadcast:
    # step 1
    link_broadcasts_xpath = "(//a[@href='/dashboard/order-broadcast'])[1]"
    create_broadcast_btn_id = "qa-broadcast-page-title-create-broadcast-button"
    number_of_broadcast_packages_id = "stepOne_order_count"
    next_btn_id = "qa-broadcast-step-one-next-buttonn"

    # Add Broadcast Details

    order_ID_input_xpath = "//input[@id='broadcastDetails_order_id']"
    loading_window_start_input = "qa-broadcast-details-form-loading-window-start"
    origin_input_id = "broadcastDetails_origin"
    number_of_trucks_id = "broadcastDetails_number_of_trucks"
    amount_currency_xpath = "//div[contains(text(),'Select Amount Currency')]"
    amount_type_xpath = "//div[contains(text(),'Select Amount Type')]"
    truck_type_xpath = "//div[normalize-space()='Select Truck Type']"
    loading_window_end_xpath = "//span[@id='broadcastDetails_loading_window_end']//i[@aria-label='icon: calendar']"
    destination_input_id = "broadcastDetails_destination"
    commodity_input_id = "broadcastDetails_commodity"
    amount_input_xpath = "//input[@id='broadcastDetails_cargo_rate_amount']"
    finish_btn_id = "qa-broadcast-details-form-submit-button"
    next_btn2_id = "qa-broadcast-step-two-next-button"
    select_transporter_btn_id = "qa-broadcast-step-three-select-transpoters-button"
    search_transporter_id = "qa-broadcast-transporters-search-input"
    select_searched_transporter_xpath = "//body[1]/div[8]/div[1]/div[2]/div[1]/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/label[1]/span[1]"
    submit_btn_id = "qa-broadcast-transporters-submit-button"
    broadcast_btn_id = "qa-broadcast-step-three-submit-button"

    def __init__(self, driver):
        self.driver = driver
    def click_broadcast(self):
        self.driver.find_element(By.XPATH, self.link_broadcasts_xpath).click()
    def click_create(self):
        self.driver.find_element(By.ID, self.create_broadcast_btn_id).click()
    def number_of_broadcast(self, number):
        self.driver.find_element(
            By.ID, self.number_of_broadcast_packages_id).clear()
        self.driver.find_element(
            By.ID, self.number_of_broadcast_packages_id).send_keys(number)
    def next_btn_create_broadcast(self):
        self.driver.find_element(By.ID, self.next_btn_id).click()

    # order details

    def order_id(self, order_id):
        self.driver.find_element(By.XPATH, self.order_ID_input_xpath).clear()
        self.driver.find_element(
            By.XPATH, self.order_ID_input_xpath).send_keys(order_id)
    def click_loading_window_start(self):
            self.driver.find_element(By.XPATH, self.order_ID_input_xpath).click()       
    def loading_window_start(self, date):
        self.driver.find_element(
            By.XPATH, self.order_ID_input_xpath).send_keys(date)
    def origin(self, origin):
        self.driver.find_element(By.ID, self.origin_input_id).send_keys(origin)
    def number_of_trucks(self, trucks_no):
        self.driver.find_element(By.ID, self.number_of_trucks_id).clear()
        self.driver.find_element(
            By.ID, self.number_of_trucks_id).send_keys(trucks_no)
    def amount_currency(self,amount):
        currency=self.driver.find_element(By.XPATH, self.amount_currency_xpath)
        dropdown=select(currency)
        dropdown.select_by_invisible_test(amount)
    def amount_type(self, type):
        self.driver.find_element(By.XPATH, self.amount_currency_xpath).clear()
        self.driver.find_element(
            By.XPATH, self.amount_type_xpath).send_keys(type)
    def truck_type(self, truck_type):
        self.driver.find_element(By.XPATH, self.truck_type_xpath).clear()
        self.driver.find_element(
            By.XPATH, self.truck_type_xpath).send_keys(truck_type)
    def click_loading_window_end(self):
            self.driver.find_element(By.XPATH, self.loading_window_end_xpath).click()        
    def loading_window_end(self, end):
        self.driver.find_element(
            By.XPATH, self.loading_window_end_xpath).send_keys(end)
    def destination(self, destination):
        self.driver.find_element(By.ID, self.destination_input_id).clear()
        self.driver.find_element(
            By.ID, self.destination_input_id).send_keys(destination)
    def commodity(self, commodity):
        self.driver.find_element(By.ID, self.commodity_input_id).clear()
        self.driver.find_element(
            By.ID, self.commodity_input_id).send_keys(commodity) 
    def amount(self, amount_price):
        self.driver.find_element(By.XPATH, self.amount_input_xpath).clear()
        self.driver.find_element(
            By.XPATH, self.amount_input_xpath).send_keys(amount_price)
    def finish_btn(self):
        self.driver.find_element(By.ID, self.finish_btn_id).click()
