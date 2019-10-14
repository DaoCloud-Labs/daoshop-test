import requests
import sys
import json
sys.path.append('.')
from lib import global_var
from lib import public_handle



class Login():
    def __init__(self):
        self.host = global_var.host
        self.url_login = global_var.url_login
        self.auto_username = global_var.auto_username
        self.auto_password = global_var.auto_password
        self.no_username = global_var.no_username
        self.wrong_password = global_var.wrong_password
        self.login_error_msg = global_var.login_error_msg


    def Login_Success(self):
        url = "http://" + self.host + self.url_login
        body = {
            "username": self.auto_username,
            "password": self.auto_password
        }
        headers = {'content-type': "application/json"}
        response = requests.post(url, data=json.dumps(body), headers=headers)
        print("url为:"+url)
        print("header为:%s" % headers)
        print("body为:%s" % body)
        # assert response.status_code == 200, "登录失败"
        if response.status_code == 200:
            print("返回内容为:%s" % response.json())
            print("测试结果:登录成功")
            return response.status_code
        else:
            print("返回内容为:%s" % response.json())
            print("测试结果:登录失败")
            return response.status_code

        # print(url)
        # print(body)
        # print(headers)


    def Login_username_no_exit(self):
        url = "http://" + self.host + self.url_login
        body = {
            "username": self.no_username,
            "password": self.auto_password
        }
        headers = {'content-type': "application/json"}
        response = requests.post(url, data=json.dumps(body), headers=headers)
        print("url为:"+url)
        print("header为:%s" % headers)
        print("body为:%s" % body)
        # assert response.status_code == 200, "登录失败"

        if response.status_code == 200:
            print("返回内容为:%s" % response.json())
            print("测试结果:登录成功")
        else:
            print("返回内容为:%s" % response.json())
            print("测试结果:登录失败")



    def Login_error_password(self):
        url = "http://" + self.host + self.url_login
        body = {
            "username": self.auto_username,
            "password": self.wrong_password
        }
        headers = {'content-type': "application/json"}
        response = requests.post(url, data=json.dumps(body), headers=headers)
        # assert response.status_code == 500, "登录失败"
        print("url为:"+url)
        print("header为:%s" % headers)
        print("body为:%s" % body)
        if response.status_code == 200:
            print("返回内容为:%s" % response.json())
            print("测试结果:登录成功")
        else:
            print("返回内容为:%s" % response.json())
            print("测试结果:登录失败")


class Registry():
    def __init__(self):
        self.registry_name = public_handle.username_random()
        self.registry_password = public_handle.username_random()
        self.url_registry = global_var.url_registry
        self.host = global_var.host

    def Registry_success(self):
        url = "http://" + self.host + self.url_registry
        body = {
            "username": self.registry_name,
            "password": self.registry_password
        }
        headers = {'content-type': "application/json"}
        response = requests.post(url, data=json.dumps(body), headers=headers)
        # assert response.status_code == 500, "登录失败"
        print("url为:"+url)
        print("header为:%s" % headers)
        print("body为:%s" % body)

        if response.status_code == 200:
            print("返回内容为:%s" % response.json())
            print("测试结果:注册成功")
        else:
            print("返回内容为:%s" % response.json())
            print("测试结果:注册失败")

class Product():
    def __init__(self):
        self.url_product = global_var.url_products
        self.host = global_var.host

    def Get_product(self):
        url = "http://" + self.host + self.url_product
        headers = {'content-type': "application/json"}
        response = requests.get(url, headers=headers)
        # assert response.status_code == 500, "登录失败"
        print("url为:"+url)
        print("header为:%s" % headers)

        if response.status_code == 200:
            print("返回内容为:%s" % response.json())
            print("测试结果:获取产品数据成功")

        else:
            print("返回内容为:%s" % response.json())
            print("测试结果:获取产品数据失败")


class Buy():
    def __init__(self):
        self.url_buy = global_var.url_buy
        self.host = global_var.host

    def Buy_product(self):
        url = "http://" + self.host + self.url_buy
        body = [
            {"productId": 1, "count": 1},
            {"productId": 2, "count": 1}
        ]
        headers = {'content-type': "application/json", 'token': "1"}
        response = requests.post(url, data=json.dumps(body), headers=headers)
        # assert response.status_code == 500, "登录失败"
        print("url为:"+url)
        print("header为:%s" % headers)
        print("body为:%s" % body)

        if response.status_code == 200:
            print("返回内容为:%s" % response.status_code)
            print("测试结果:购买成功")
        else:
            print("返回内容为:%s" % response.json())
            print("测试结果:购买失败")




    def Buy_product_error(self):
        url = "http://" + self.host + self.url_buy
        body = [{"productId": "xxxx", "count": 1}]
        headers = {'content-type': "application/json", 'token': "1"}
        response = requests.post(url, data=json.dumps(body), headers=headers)
        # assert response.status_code == 500, "登录失败"
        print("url为:"+url)
        print("header为:%s" % headers)
        print("body为:%s" % body)

        if response.status_code == 200:
            print("测试结果:购买成功")
            print(response.status_code)
        else:
            print("测试结果:购买失败")
            print(response.json())


def login_success():
    print("API_test:Login")
    print("======================")
    print("01用户名密码正确")
    login = Login()
    login.Login_Success()


def login_error_username():
    print("API_test:Login")
    print("======================")
    print("02用户名错误")
    login = Login()
    login.Login_username_no_exit()


def login_error_password():
    print("API_test:Login")
    print("======================")
    print("03密码错误")
    login = Login()
    login.Login_error_password()

def registry_success():
    print("API_test:Registry")
    print("======================")
    print("01用户名密码注册")
    registry = Registry()
    registry.Registry_success()


def get_product():
    print("API_test:product")
    print("======================")
    print("01获取产品数据")
    product = Product()
    product.Get_product()


def buy_product():
    print("API_test:buy_product")
    print("======================")
    print("01购买产品_body正确")
    buy = Buy()
    buy.Buy_product()


def buy_product_error():
    print("API_test:buy_product")
    print("======================")
    print("02购买产品_body出错")
    buy = Buy()
    buy.Buy_product_error()








if __name__ == '__main__':
    # print("API_test:Login")
    # print("======================")
    # print("01登录成功")
    # login = Login()
    # login.Login_Success()
    # print("======================")
    # print("02用户名错误")
    # login.Login_username_no_exit()
    # print("======================")
    # print("03密码错误")
    # login.login_error_password()


    # print("API_test:Registry")
    # print("======================")
    # print("01注册成功")
    # registry = Registry()
    # registry.registry_success()
    #
    # print("API_test:product")
    # print("======================")
    # print("01获取产品数据")
    # product = Product()
    # product.get_product()

    print("API_test:buy_product")
    print("======================")
    print("01购买产品成功")
    buy = Buy()
    buy.buy_product()
    print("02购买产品失败")
    buy.buy_product_error()

