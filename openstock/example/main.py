from openstock.stock.client import StockClient

# 初始化
stock_client = StockClient()


# 获取历史数据
stock_bars = stock_client.get_stock_bars(symbol="sz000002", start_date="20240901")
print(stock_bars)


