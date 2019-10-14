import sys
sys.path.append('.')
from lib.daoshop_API import Login,Product,Registry,Buy


class Mac_API(Login):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
