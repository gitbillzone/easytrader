import datetime
import os
import time
import unittest
from unittest import mock
import easytrader

from easytrader.xq_follower import XueQiuFollower
from easytrader import server

class TestTongHuaShun(unittest.TestCase):
    def test_run(self):
        server.run(port=1430)

        # print("xxxxxx")
        # user = easytrader.use('universal_client')
        # user.connect(r'C:\同花顺软件\同花顺\xiadan.exe')
        # user.enable_type_keys_for_editor()
        # print(user.balance)
        # print('local time : ' + str(time.time()))
        # user.buy('sh601919', price=20,amount=100)

if __name__ == '__main__':
    print("xxxxxxxx")
