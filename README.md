# A util for US stock market

## 简介

一个美股行情工具包，可以用来获取美股股票列表、实时行情、历史k线数据。

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

token = '8aa9be32f402301d' 
stock_client = StockClient(token)
```

token申请地址： https://stock.mypython.me/app/apply_token

- 获取美股代码列表

```python
stock_list = stock_client.get_stock_list()
print(stock_list)
```

- 获取实时行情

```python
stock_quote = stock_client.get_stock_quote(query=['BABA','JD'])
print(stock_quote)
```

- 获取历史行情数据

```python
stock_bars = stock_client.get_stock_bars(query=['BABA','JD'])
print(stock_bars)
```

## 赞助作者

wx：285126081
