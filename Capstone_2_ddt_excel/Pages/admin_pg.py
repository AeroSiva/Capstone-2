from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Locators.locators import Orangehrm_locators2
from Data.data import OrangeHrm_data2
from Utils.utils import Util2


class Admin_cls:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait =wait

    def get_tiltle(self):
        actual_title = self.driver.title
        return actual_title
    

    def validate_title(self,expected_title):
        actual_title = self.get_tiltle()
        assert actual_title == expected_title
        return actual_title
    
    # Get headers from Admin module page
    def get_headers(self):
        header_lst = []
        header_elements_e = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,Orangehrm_locators2().header_elements_xpath)))
        for element in header_elements_e:
            headers_in_nav = element.text
            header_lst.append(headers_in_nav)
        print("Header list from get_headers method : ",header_lst)
        return header_lst
    
    
    # Checking whether the expected header list mathes headers in webpage
    def validate_header(self,h1,h2,h3,h4,h5,h6,h7):
        header_lst = self.get_headers()
        missing_headers = []
        expected_header_lst = [h1,h2,h3,h4,h5,h6,h7]
        print("Expected header list from validate_header methpd : ",expected_header_lst)
        for h in expected_header_lst:
            if h in header_lst:
                print(h,": present in header webpage.")
            else:
                print(h,"Not present in header webpage. Test fails.")
                missing_headers.append(h)

        # Raise an exception if there are missing headers
        if missing_headers:
            raise AssertionError(f"Missing headers: {', '.join(missing_headers)}")
        
    def validate_isdisplay_header(self,row,expected_result):
        try:

            user_Management = self.wait.until(EC.presence_of_element_located((By.XPATH,Orangehrm_locators2().ad_pg_user_management)))

            job = self.wait.until(EC.presence_of_element_located((By.XPATH,Orangehrm_locators2().ad_pg_job)))
            
            organization = self.wait.until(EC.presence_of_element_located((By.XPATH,Orangehrm_locators2().ad_pg_org)))
            
            qualification = self.wait.until(EC.presence_of_element_located((By.XPATH,Orangehrm_locators2().ad_pg_qualification)))
            
            nationalities = self.wait.until(EC.presence_of_element_located((By.XPATH,Orangehrm_locators2().ad_pg_nationalities)))
            
            corporate_branding = self.wait.until(EC.presence_of_element_located((By.XPATH,Orangehrm_locators2().ad_pg_corporate_branding)))
            
            configuration = self.wait.until(EC.presence_of_element_located((By.XPATH,Orangehrm_locators2().ad_pg_configuration)))

            headerlist = [user_Management,job,organization,qualification,nationalities,corporate_branding,configuration]
            
            actual_result = ''
            visible_headers = []
            invisible_headers = []
            for element in headerlist:
                if element.is_displayed():
                    visible_headers.append(element.text)
                else:
                    invisible_headers.append(element.text)

            if invisible_headers:
                actual_result = f"{','.join(invisible_headers)}is/are not visible"
            else:
                actual_result = f"Header elements {','.join(visible_headers)} are visible"

            return actual_result
        
        except Exception as e:
            print("Checking whether the header elements are displayed or not : ",e)


    # Get all the side pane elements
    def get_side_pane(self):
        try:
            # Wait for the elements to get loaded
            side_pane_mes =  self.wait.until(EC.presence_of_all_elements_located((By.XPATH,Orangehrm_locators2().side_pane_elements_xpath)))
            side_pane_text_list = []
            for element in side_pane_mes:
                side_pane_ele_text = element
                side_pane_text_list.append(side_pane_ele_text)
            return side_pane_text_list
        except Exception as e:
            print("Error : Getting side pane elements failed : ",e)
    
    
    # Validate whether all the elements are displayed or not
    def validate_visibility_side_panel_elements(self):
        try:
            visible_side_pane_text_list = []
            invisible_side_pane_text_list = []
            side_pane_text_list = self.get_side_pane()
            for element in side_pane_text_list:
                if element.is_displayed():
                    visible_side_pane_text_list.append(element.text)
                else:
                    invisible_side_pane_text_list.append(element.text)
            
            actual_result = ''
            if invisible_side_pane_text_list:
                actual_result = ','.join(invisible_side_pane_text_list)
            else:
                actual_result = ','.join(visible_side_pane_text_list)

            return actual_result
        except Exception as e:
            print("Error : validate_visibility_side_panel_elemen method failed : ",e)

    # Test case to check whether the header elements are visible and written in excel and given to pytest
    def tc_validate_title_isdisplay_header(self,row,expected_result,expected_title):
        try:
            actual_title = self.validate_title(expected_title)
            actual_header = self.validate_isdisplay_header(row,expected_result)
            actual_result = f"Title : {actual_title} Side pane elements {actual_header} are displayed"
            try:
                Util2.write_date_time_actual_result_in_excel(self,row,actual_result)
                Util2.write_test_pass_fail_in_excel(self,row,actual_result,expected_result)
            except Exception as e:
                print("Error writing date/time or Checking actual result against expected and wrinting whether test pass or fail failed: ",e)
                
            return actual_result
        except Exception as e:
            print("Error : tc_validate_title_isdisplay_header failed : ",e)

    def tc_validate_visibility_side_panel_elements(self,row,expected_result):
        try:
            print("Test case for checking visibilty of side pane element running")
            actual_result = self.validate_visibility_side_panel_elements()
            actual_result = f"Side pane elements {actual_result} are displayed"
            try:
                Util2.write_date_time_actual_result_in_excel(self,row,actual_result)
                Util2.write_test_pass_fail_in_excel(self,row,actual_result,expected_result)
            except Exception as e:
                print("Error writing date/time or Checking actual result against expected and wrinting whether test pass or fail failed: ",e)
            
            actual_result = actual_result
            return actual_result
        except Exception as e:
            print("Error : tc_validate_visibility_side_panel_elements failed : ",e)