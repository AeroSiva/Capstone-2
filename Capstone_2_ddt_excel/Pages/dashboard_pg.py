from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import Orangehrm_locators2
from Data.data import OrangeHrm_data2
from Utils.utils import Util2


class Dashboard_cls:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def click_admin(self):
        admin_module_e = self.wait.until(EC.presence_of_element_located((By.XPATH,Orangehrm_locators2().admin_module_xpath)))
        admin_module_e.click()
        Util2.wait_for_url_change(self,old_url=OrangeHrm_data2().admin_pg_url)
        print("Clicked admin")
        # loads Admin page 