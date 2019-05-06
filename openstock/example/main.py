from openstock.stock.client import StockClient

# 初始化
token = "8aa9be32f402301d"
stock_client = StockClient(token)

# 获取股票列表
stock_list = stock_client.get_stock_list()
print(stock_list)

# 获取实时行情
stock_quote = stock_client.get_stock_quote(query=['BABA','JD'])
print(stock_quote)
#
# 获取历史数据
stock_bars = stock_client.get_stock_bars(query=['BABA','JD'])
print(stock_bars)


