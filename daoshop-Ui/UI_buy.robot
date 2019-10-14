*** Settings ***
Library           Selenium2Library
Library           json
Library           ../lib/public_handle.py
Variables         ../lib/global_var.py
Resource          flow.robot
Library           DatabaseLibrary

*** Test Cases ***
ui_buy_success
    [Setup]
    login
    ${productId}    product_elem_click
    order_a_click
    ${name}    get_buy_product_name
    buy_elem_click
    return_order

    [Teardown]    close_driver
