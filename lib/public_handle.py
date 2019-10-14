import random

def decode(comtext):
    re_data = comtext.decode('utf-8')
    return re_data

def username_random():
    name = '"test{}"'.format(random.randint(100000, 999999))
    return name
