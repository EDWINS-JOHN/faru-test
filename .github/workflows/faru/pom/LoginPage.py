from selenium.webdriver.common.by import By



class LoginPage:
    
       input_email_id ="qa-login-email"
       input_password_id="qa-login-password"
       login_button_id="qa-login-submit"
       user_profile_menu_xpath="//div[@class='user-profile-icon']//i[@aria-label='icon: user']"
       logout_button_xpath="//span[@id='qa-logout']"
       
       
       def __init__(self,driver):
              self.driver=driver
              
              
              
       def get_email(self,email):
              self.driver.find_element(By.ID,self.input_email_id).clear()
              self.driver.find_element(By.ID,self.input_email_id).send_keys(email)
              
       def get_password(self,password):
              self.driver.find_element(By.ID,self.input_password_id).clear()
              self.driver.find_element(By.ID,self.input_password_id).send_keys(password)
              
              
       def click_login(self):
              self.driver.find_element(By.ID,self.login_button_id).click()
              
       def user_Profile(self):
              self.driver.find_element(By.XPATH,self.user_profile_menu_xpath).click()
              
       def click_logout(self):
              self.driver.find_element(By.XPATH,self.logout_button_xpath).click()