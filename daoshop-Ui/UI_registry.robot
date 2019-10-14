*** Settings ***
Library           Selenium2Library
Library           json
Library           ../lib/public_handle.py
Variables         ../lib/global_var.py
Resource          flow.robot

*** Test Cases ***
ui_registry_success
    Open Browser    ${ui_registry}    chrome
    ${username}    username_random
    ${password}    Set Variable    ${auto_password}
    registry_username_input    ${username}
    registry_password_input    ${password}
    registry_button_click
    login_username_input    ${username}
    login_password_input    ${password}
    login_button_click
    user_a_click
    Element Should Contain     //*[@id="page-user"]/div/div    ${username}
    [Teardown]    close_driver
