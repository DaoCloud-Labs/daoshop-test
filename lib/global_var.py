#!/usr/bin/env python3

import os

host = os.getenv('DS_HOST') if os.getenv('DS_HOST') else "10.15.160.1:30965"


url_login = "/demo/user/v1/login"
url_products = "/demo/product/v1/products"
url_registry = "/demo/user/v1/registry"
url_buy = "/demo/product/v1/products/buy"

auto_username = 'autotest'
auto_password = 'autopassword'
no_username = 'user_not_exit'
wrong_password = '12343244234134'
mysql_host = '"10.122.22.209"'
mysql_port = '3306'
mysql_user = '"root"'
mysql_pwd = '"Mac_034567"'
mysql_product_database = '"product"'
mysql_user_database = '"mac_user_center"'
mysql_order_database = '"order"'

login_error_msg = "username or password not right!"


ui_registry = os.getenv('DS_UI_REGISTRY') if os.getenv('DS_UI_REGISTRY') else "http://10.15.160.1:30965/registry"
ui_user = os.getenv('DS_UI_USER') if os.getenv('DS_UI_USER') else "http://10.15.160.1:30965/user"
ui_login = os.getenv('DS_UI_LOGIN') if os.getenv('DS_UI_LOGIN') else "http://10.15.160.1:30965/login"
ui_auto_username = auto_username
ui_auto_password = auto_password