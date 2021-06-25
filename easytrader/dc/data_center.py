from easytrader.main.handle_quotes import *
import easytrader

g_datacenter_instance = None

class DataCenter:
    def __init__(self):
        self.hanle_quotes = HanleQuotes()
        self.init_easytrader()


    def init_easytrader(self):
        self.user = easytrader.use('universal_client')
        self.user.connect(r'C:\同花顺软件\同花顺\xiadan.exe')
        self.user.enable_type_keys_for_editor()

    def get_user(self):
        return self.user

    def get_handle_quotes(self):
        return self.hanle_quotes

    @staticmethod
    def get_instance():
        global g_datacenter_instance
        if g_datacenter_instance == None:
            g_datacenter_instance = DataCenter()
        return  g_datacenter_instance