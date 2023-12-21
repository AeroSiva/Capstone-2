class Orangehrm_locators2:
    # Login page
    username_ip_name = 'username'
    password_ip_name = 'password'
    login_btn_xpath = '//button[@type="submit"]'
    forgot_pw_xpath = '//div[@class="orangehrm-login-forgot"]/p[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]'
    invalid_login_alert_css = 'div.oxd-alert-content.oxd-alert-content--error>p'


    # Reset password page
    rs_pg_username_name = 'username'
    rs_pg_cancel_xpath = '//button[text()=" Cancel "]'
    rs_pg_submit_xpath = '//button[text()=" Reset Password "]'


    # Reset message sent page
    rm_password_lim_xpath ='//div[@class="orangehrm-card-container"]/h6'


    # Side panel / Dashboard page
    userdropdown_icon_xpath = '//div[@class="oxd-topbar-header-userarea"]//i'
    logout_link_xpath = '//a[@href="/web/index.php/auth/logout"]'
    side_pane_elements_xpath = '//aside//ul/li/a'
    admin_module_xpath = '//aside//ul/li/a[@href="/web/index.php/admin/viewAdminModule"]/span' #'//a[@href="/web/index.php/"]'
    pim_module_xpath = '//aside//ul/li/a[@href="/web/index.php/pim/viewPimModule"]/span'
    leave_module_xpath = '//aside//ul/li/a[@href="/web/index.php/leave/viewLeaveModule"]/span'
    time_module_xpath = '//aside//ul/li/a[@href="/web/index.php/time/viewTimeModule"]/span'
    recruitment_module_xpath = '//aside//ul/li/a[@href="/web/index.php/recruitment/viewRecruitmentModule"]/span'
    my_info_module_xpath = '//aside//ul/li/a[@href="/web/index.php/pim/viewMyDetails"]/span'
    performance_module_xpath = '//aside//ul/li/a[@href="/web/index.php/performance/viewPerformanceModule"]/span'
    dashboard_module_xpath = '//aside//ul/li/a[@href="/web/index.php/dashboard/index"]/span'
    directory_module_xpath = '//aside//ul/li/a[@href="/web/index.php/directory/viewDirectory"]/span'
    maintanence_module_xpath = '//aside//ul/li/a[@href="/web/index.php/maintenance/viewMaintenanceModule"]/span'
    claim_modulo_xpath = '//aside//ul/li/a[@href="/web/index.php/claim/viewClaimModule"]/span'
    buzz_modulo_xpath = '//aside//ul/li/a[@href="/web/index.php/buzz/viewBuzz"]/span'


    # Admin page
    header_elements_xpath = '//header[@class="oxd-topbar"]/div[@class="oxd-topbar-body"]/nav/ul/li'
    ad_pg_user_management = '//header[@class="oxd-topbar"]/div[@class="oxd-topbar-body"]/nav/ul/li/span[text()="User Management "]'
    ad_pg_job = '//header[@class="oxd-topbar"]/div[@class="oxd-topbar-body"]/nav/ul/li/span[text()="Job "]'
    ad_pg_org = '//header[@class="oxd-topbar"]/div[@class="oxd-topbar-body"]/nav/ul/li/span[text()="Organization "]'
    ad_pg_qualification = '//header[@class="oxd-topbar"]/div[@class="oxd-topbar-body"]/nav/ul/li/span[text()="Qualifications "]'
    ad_pg_nationalities = '//header[@class="oxd-topbar"]/div[@class="oxd-topbar-body"]/nav/ul/li/a[text()="Nationalities"]'
    ad_pg_corporate_branding = '//header[@class="oxd-topbar"]/div[@class="oxd-topbar-body"]/nav/ul/li/a[text()="Corporate Branding"]'
    ad_pg_configuration = '//header[@class="oxd-topbar"]/div[@class="oxd-topbar-body"]/nav/ul/li/span[text()="Configuration "]'
    
    