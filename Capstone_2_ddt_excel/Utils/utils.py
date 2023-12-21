from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import Orangehrm_locators2
import time

class Util2:
    def __init__(self,driver,wait):
         self.driver = driver
         self.wait = wait

    def login_orangehrm(self,username,password):
        username_ip_box = self.wait.until(EC.element_to_be_clickable((By.NAME,Orangehrm_locators2().username_ip_name)))
        username_ip_box.clear()
        username_ip_box.send_keys(username)
        password_ip_box = self.wait.until(EC.element_to_be_clickable((By.NAME,Orangehrm_locators2().password_ip_name)))
        password_ip_box.clear()
        password_ip_box.send_keys(password)
        login_btn=self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators2().login_btn_xpath)))
        login_btn.click()
        print("Logged in Orange Hrm")

    def wait_for_url_change(self, old_url, timeout=4):
        start_time = time.time()

        while time.time() - start_time < timeout:
            if self.driver.current_url != old_url:
                return True
            time.sleep(0.5)
        return False

    def logout_Orangehrm(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators2.userdropdown_icon_xpath))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators2.logout_link_xpath))).click()
            print("Logged out")
        except Exception as e:
            print("Log out error : ", e)

    def notification_text_from_dynamic_notification(self,locator_type,locator,add_element_locator):
        try:
            notification_container = self.wait.until(
                                EC.presence_of_element_located((locator_type, locator)))

                # Wait for additional elements to be present within the notification container
            additional_elements = self.wait.until(
                                EC.presence_of_all_elements_located((locator_type, add_element_locator)))

            # Get the text of the notification
            notification_text = notification_container.text
            # Iterate over additional elements and perform actions
            '''for element in additional_elements:
                # Do something with each additional element
                    element_text = element.text
                    print("Additional Element Text:", element_text)
            '''
            return notification_text
        except Exception as e:
            print("Fetching message from dymaic notification error : ",e)

    def write_date_time_actual_result_in_excel(self,row,actual_result):
        try:
            date = self.date.strftime("%x")
            self.excel_func.write_data(row, 4, date)
            time = self.date.strftime("%X")
            self.excel_func.write_data(row,5,time)
            self.excel_func.write_data(row, 11, actual_result)
        except Exception as e:
            print("Writing date time or actual result error : ",e)

    def write_test_pass_fail_in_excel(self,row,act_res,exp_res):
        try:
            test_result = ''
            if act_res == exp_res:
                test_result = 'Test Passed'
            else:
                test_result = 'Test Failed'
            self.excel_func.write_data(row,13,test_result)
        except Exception as e:
            print("Writing or comparing the actual result with expected faild : ",e)

    