import pytest
from Pages.login_page import Login_page_cls
from Excel_Functions.excel_functions import Excel_Functions
from Data.data import OrangeHrm_data2


@pytest.mark.usefixtures("setup")
class Test_login_logout:

     # TC_pim_01
     @pytest.mark.parametrize(" row, username_da, expected_result", Excel_Functions
                         (OrangeHrm_data2.excel_file_name,OrangeHrm_data2.excel_reset_pw_t_sheet).read_excel_data_p2_t1())
     def test_forget_password_link(self, row, username_da,expected_result):
          try:
               print("Initiating instance of Firefox")
               lp = Login_page_cls(self.driver,self.wait)
               
               print("Step 1")
               actual_result = lp.tc_validate_forget_link_login(row,username_da,expected_result)
               assert actual_result == expected_result
          except Exception as e:
               print("Error : TC_pim_01 : test_forget_password_link failed : ",e)
     
     # TC_pim_02
     # Validating title and header in admin page test
     @pytest.mark.parametrize("row,expected_result,username,password,expected_title,user_Management,job,organization,qualification,nationalities,corporate_branding,configuration", Excel_Functions
                         (OrangeHrm_data2.excel_file_name,OrangeHrm_data2.validate_title_header_sheet).read_excel_data_p2_t2())
     def test_validate_title_header(self,row,expected_result,username,password,expected_title,user_Management,job,organization,qualification,nationalities,corporate_branding,configuration):
          try:
               
               print("Step 1")
               tp =Login_page_cls(self.driver,self.wait)
               tp.login_orangehrm(username,password)
               # Navigated into Dashboard page
               
               print("Step 2")
               tp.click_admin()
               # Navigated to admin page
               
               print("Step 3")
               tp.validate_header(user_Management,job,organization,qualification,nationalities,corporate_branding,configuration)
               actual_result = tp.tc_validate_title_isdisplay_header(row,expected_result,expected_title)
               
               print("Step 4")
               tp.logout_Orangehrm()
               assert actual_result == expected_result
          except Exception as e:
               print("Error : TC_pim_02 : test_validate_title_header ",e)

     # TC_pim_03
     # Validating menu items 
     @pytest.mark.parametrize("row,username,password,expected_result",Excel_Functions(excel_file_name="Capstone_2.xlsx",excel_sheet_name="Sheet4").read_excel_data_p2_t3())
     def test_validate_admin_menu(self,row,username,password,expected_result):
          try:
               print("Step 1")
               tp = Login_page_cls(self.driver,self.wait)
               tp.login_orangehrm(username,password)
               # Navigated into Dashboard page
               
               print("Step 2")
               tp.click_admin()
               # Navigate to admin page
               
               print("Step 3")
               actual_result = tp.tc_validate_visibility_side_panel_elements(row,expected_result)
               
               print("Step 4")
               tp.logout_Orangehrm()
               assert actual_result == expected_result
          except Exception as e:
               print("Error : TC_pim_03 : test_validate_admin_menu ",e)