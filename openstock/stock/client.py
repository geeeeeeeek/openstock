
import akshare as ak


class StockClient(object):

    def get_stock_bars(self, symbol="", start_date=None, end_date=None):
        df = ak.stock_zh_a_daily(symbol=symbol, start_date=start_date, end_date=end_date)
        df = df[['date', 'open', 'high', 'low', 'close', 'volume']]
        df = df.rename(columns={'date': 'datetime'})
        df['openinterest'] = 0
        return df
