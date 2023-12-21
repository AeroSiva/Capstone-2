from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import datetime
from Locators.locators import Orangehrm_locators2
from Data.data import OrangeHrm_data2
from Excel_Functions.excel_functions import Excel_Functions
from Utils.utils import Util2
from Pages.rest_user_login_pg import Rest_password_cls
from Pages.dashboard_pg import Dashboard_cls
from Pages.admin_pg import Admin_cls



class Login_page_cls(Orangehrm_locators2,OrangeHrm_data2,Util2,Rest_password_cls,Dashboard_cls,Admin_cls):
    def __init__(self,driver,wait):
        super().__init__(driver,wait)
        self.driver = driver
        self.wait = wait
        self.action = ActionChains(self.driver)
        self.date = datetime.datetime.now()
        self.excel_func = Excel_Functions(OrangeHrm_data2().excel_file_name, OrangeHrm_data2().excel_sheet_name)
        self.row = self.excel_func.row_count()
    
    
    # Login test case for valid and invalid username and password 
    
    