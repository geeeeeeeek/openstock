import requests

from openstock.common.helpers import is_empty
from openstock.common.params import STOCK_LIST_URL, STOCK_QUOTE_URL, STOCK_BARS_URL


class StockClient(object):

    def __init__(self, token=''):
        self.token = token

    def get_stock_list(self):
        """
        获取股票代码和名称
        :return:
        """

        if is_empty(self.token):
            print("Token can not be EMPTY")
            return

        payload = {'token':self.token}
        r = requests.get(STOCK_LIST_URL, params=payload)

        if r.status_code == 200:
            obj = r.json()
            if obj['code'] == 0:
                return obj['data']
            else:
                print(obj['msg'])
        else:
            print("服务器异常 error_code:"+str(r.status_code))


    def get_stock_quote(self, query=[]):
        """
        获取个股行情
        :param query: 股票代码
        :return:
        """

        if is_empty(self.token):
            print("Token can not be EMPTY")
            return

        if len(query) <= 0:
            print("Query can not be empty")
            return

        query = ','.join(query)

        payload = {'token':self.token, 'query': query}
        r = requests.get(STOCK_QUOTE_URL, params=payload)

        if r.status_code == 200:
            obj = r.json()
            if obj['code'] == 0:
                return obj['data']
            else:
                print(obj['msg'])
        else:
            print("服务器异常 error_code:"+str(r.status_code))


    def get_stock_bars(self, query=[], period='day', limit=20,
                       begin_time=-1, end_time=-1,right='br'):
        """
        获取个股行情
        :param period: day/week/month/year/1min/5min/15min/30min/60min
        :param limit: 数据条数
        :param begin_time:
        :param end_time:
        :param right: 复权方式 br/nr
        :param query: 股票代码
        :return:
        """

        if is_empty(self.token):
            print("Token can not be EMPTY")
            return

        if len(query) <= 0:
            print("Query can not be empty")
            return

        query = ','.join(query)

        payload = {'token':self.token, 'query': query, 'limit':limit, 'period':period,
                   'begin_time':begin_time, 'end_time':end_time, 'right':right}
        r = requests.get(STOCK_BARS_URL, params=payload)

        if r.status_code == 200:
            obj = r.json()
            if obj['code'] == 0:
                return obj['data']
            else:
                print(obj['msg'])
        else:
            print("服务器异常 error_code:"+str(r.status_code))

