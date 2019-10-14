
*** Keywords ***
close_driver
    Close Browser


# 输入注册账号
registry_username_input
    [Arguments]    ${username}
    Input Text    //input[@type='text']    ${username}

# 输入注册密码
registry_password_input
    [Arguments]    ${password}
    Input Text    //input[@type='password']    ${password}

# 点击注册
registry_button_click
    Click Button    //button[@type='button']
    sleep    2s

# 输入登录账户
login_username_input
    [Arguments]    ${username}
    Input Text    //input[@type='text']    ${username}

# 输入登录密码
login_password_input
    [Arguments]    ${password}
    Input Text    //input[@type='password']    ${password}

# 点击登录按钮
login_button_click
    Click Button    //*[@id="page-user"]/div/button[1]
    sleep    2s

# 点击用户头像
user_a_click
    Click Element    //a[@class='']
    sleep    2s

# 登录操作
login

    Open Browser    ${ui_login}    chrome
    login_username_input    ${ui_auto_username}
    login_password_input    ${ui_auto_password}
    login_button_click

# 点击购物商品
product_elem_click
    ${index}    evaluate    random.randint(0, 2)    random
    ${path}    Set Variable    //*[@id="itemundefined"]
    Click Element    ${path}
    [Return]    ${index}

# 点击购物车
order_a_click
    Click Element    //a[@class='mr20']
    sleep    2s

# 获取购买商品名称
get_buy_product_name
    ${name}    GET TEXT    //p[@class="cast-goods-title"]
    [Return]    ${name}

# 点击购买按钮
buy_elem_click
    Click Element    //div[@class='action-btn buy-btn']

# 返回购物页进入订单
return_order
    Click Element     //*[@id="page-cast"]/header/div/a
    Click Element    //html/body/div/header/div/div/a[2]
    Click Element    //*[@id="page-user"]/header/div/div/a/span



# 连接数据库查看信息
get_order_from_mysql_by_autotest
    log    mysql connect
    Connect to Database Using Custom Params    pymysql    host=${mysql_host},port=${mysql_port},user=${mysql_user},password=${mysql_pwd}, database=${mysql_user_database}
    log    mysql connected
    ${userId}    query    select id from t_product where username = ${auto_username} and password = ${auto_password}
    Connect to Database Using Custom Params    pymysql    host=${mysql_host},port=${mysql_port},user=${mysql_user},password=${mysql_pwd}, database=${mysql_order_database}
    ${order_info}    query    select id, amount, user_id from t_order where user_id = ${userId}[0][0] order by id desc limit 1
    ${order_id}    Set Variable    ${order_info}[0][0]
    ${items_info}    query    select count, product_name from t_item where items_id = ${order_id}
    ${expect_count}    Set Variable    ${items_info}[0][0]
    ${expect_name}    Set Variable    ${items_info}[0][1]
    [Return]    ${expect_count}    ${expect_name}
