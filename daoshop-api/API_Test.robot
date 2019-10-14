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
    login_success

Login_error_username
    [Setup]
    log     ${host}
    log     ${url_login}
    login_error_username

Login_error_password
    [Setup]
    log     ${host}
    log     ${url_login}
    login_error_password


Registry_success
    log     ${host}
    log     ${url_registry}
    registry_success


Get_product
    log     ${host}
    log     ${url_products}
    get_product


Buy_product
    log     ${host}
    log     ${url_buy}
    buy_product


Buy_product_error
    log     ${host}
    log     ${url_buy}
    buy_product


