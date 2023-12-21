from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Locators.locators import Orangehrm_locators2
from Data.data import OrangeHrm_data2
from Utils.utils import Util2


class Rest_password_cls:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def tc_validate_forget_link_login(self,row,username_da,expected_result):
            '''
            Test case for validating forge link running")
            '''
            try:
                username_ipe = self.wait.until(EC.element_to_be_clickable((By.NAME,Orangehrm_locators2().username_ip_name)))
                username_ipe.click()
                username_ipe.send_keys(username_da)
                forgot_pw_lie = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators2().forgot_pw_xpath)))
                forgot_pw_lie.click()
                print("Forgot password link clicked")
                Util2.wait_for_url_change(self,old_url=OrangeHrm_data2().login_url,timeout=4)
                username_ipe = self.wait.until(EC.element_to_be_clickable((By.NAME,Orangehrm_locators2().rs_pg_username_name)))
                username_ipe.send_keys(username_da)
                reset_bute = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators2().rs_pg_submit_xpath)))
                reset_bute.click()
                print("Reset button clicked")
                # This method checks for any change in url if url doesn' change return False
                Util2.wait_for_url_change(self,old_url=OrangeHrm_data2().rest_pw_url)
                reset_link_sent_message_e = self.wait.until(EC.presence_of_element_located((By.XPATH,Orangehrm_locators2().rm_password_lim_xpath)))
                actual_result = reset_link_sent_message_e.text
                print(actual_result)
                self.driver.back()
                self.driver.back()
            except Exception as e:
                print("Trying login error : ",e)
            
            try:
                Util2.write_date_time_actual_result_in_excel(self,row,actual_result)
                Util2.write_test_pass_fail_in_excel(self,row,actual_result,expected_result)
                print("Written actual result date and time in Capstone_2.xlsx Sheet1")
            except Exception as e:
                print("Writing in excel or Checking actual result against expected and wrinting whether test pass or fail failed: ",e)
            
            return actual_result