*** Settings ***
# Library           HttpLibrary.HTTP
Library           json
Library           Collections
# Library           DatabaseLibrary
Library           ../lib/public_handle.py
Variables         ../lib/global_var.py
Library           ../lib/daoshop_API.py

*** Test Cases ***
Login_success
    [Setup]
    log     ${host}
    log     ${url_login}
    ${result}    login_success
    should be equal  ${result}   ${True}


Login_error_username
    [Setup]
    log     ${host}
    log     ${url_login}
    ${result}    login_error_username
    should be equal    ${result}   ${False}

Login_error_password
    [Setup]
    log     ${host}
    log     ${url_login}
    ${result}    login_error_password
    should be equal    ${result}   ${False}


Registry_success
    log     ${host}
    log     ${url_registry}
    ${result}   registry_success
    should be equal    ${result}   ${True}


Get_product
    log     ${host}
    log     ${url_products}
    ${result}    get_product
    should be equal    ${result}   ${True}


Buy_product
    log     ${host}
    log     ${url_buy}
    ${result}  buy_product
    should be equal    ${result}   ${True}


Buy_product_error
    log     ${host}
    log     ${url_buy}
    ${result}    buy_product_error
    should be equal    ${result}   ${False}


