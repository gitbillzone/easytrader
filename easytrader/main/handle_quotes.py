from easytrader.dc import data_center
import json

class HanleQuotes:
    def __init__(self):
        self.monitor_stock_dict = {}
        self.basic_stock_list = []
        self.traded_stock_dict = {}


    def update_stock(self,stock_dict):
        self.monitor_stock_dict.clear()
        for stock_id in self.basic_stock_list:
            limit_price = stock_dict.get(stock_id)
            if limit_price is None:
                continue
            self.monitor_stock_dict[stock_id] = limit_price


    def get_limit_price(self,stock_id):
        return self.monitor_stock_dict.get(stock_id)

    def get_monitor_stocks(self):
        self.monitor_stock_dict.keys()

    def insert_traded_stock(self,stock_id):
        self.traded_stock_dict[stock_id] = 0

    def is_traded(self, stock_id):
        if self.traded_stock_dict.get(stock_id) is None:
            return False

        return True




def dispatch_quotes(pUderdata,id,sResult,lens,errorcode,reserved):
    tick_data = json.loads(sResult)
    for stock_data in tick_data['tables']:
        code = stock_data['thscode']
        if data_center.DataCenter.get_instance().get_handle_quotes().is_traded(code):
            continue
        limit_price = data_center.DataCenter.get_instance().get_handle_quotes().get_limit_price(code)
        if stock_data['table']['ask1'][0] >= limit_price or stock_data['table']['ask2'][0] >= limit_price or stock_data['table']['ask3'][0] >= limit_price or stock_data['table']['ask4'][0] >= limit_price or stock_data['table']['ask5'][0] >= limit_price:
            data_center.DataCenter.get_instance().get_user().buy(code,price=limit_price,amount=100)
            data_center.DataCenter.get_instance().get_handle_quotes().insert_traded_stock(code)




