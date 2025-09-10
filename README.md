# A util for stock market

## 简介

一个股票行情工具包，可以用来获取股票历史k线数据。

## 环境

python 3.x

## 安装 
 
```
pip install openstock
```

## 使用

- 初始化

```python
from openstock.stock.client import StockClient
stock_client = StockClient()
```



- 获取历史行情数据

```python
stock_bars = stock_client.get_stock_bars(symbol="sz000002")
print(stock_bars)
```

Thanks
