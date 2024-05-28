## 1. 简介
CryptoQuant API 是一个用于加密货币量化交易的 FastAPI 服务。该 API 提供了一系列端点，用于获取市场数据、下单、查询账户余额以及管理模拟交易模式。

## 2. 使用说明
### 2.1. 环境准备
首先确保你的系统已安装 Python 3.x。
安装 FastAPI 和 Uvicorn：
pip install fastapi uvicorn
### 2.2. 运行服务
在命令行中执行以下命令以运行 CryptoQuant API 服务：

uvicorn main:app --reload
服务将在默认端口 127.0.0.1:8000 上运行。
### 2.3. API 使用示例
可以使用 cURL 或其他 HTTP 客户端工具来与 API 进行交互。

### 获取账户余额
curl -X GET "http://127.0.0.1:8000/balance"

### 下单
curl -X POST "http://127.0.0.1:8000/order" -H "Content-Type: application/json" -d '{
  "instId": "BTC-USDT",
  "side": "buy",
  "ordType": "limit",
  "sz": "1",
  "px": "30000"
}'

### 获取市场数据
curl -X GET "http://127.0.0.1:8000/market/BTC-USDT"

### 启用模拟交易模式
curl -X POST "http://127.0.0.1:8000/enable_simulation"

### 禁用模拟交易模式
curl -X POST "http://127.0.0.1:8000/disable_simulation"
## 3. 错误处理
如果请求出现错误，API 将返回相应的 HTTP 状态码和错误详情信息。
## 4. 注意事项
请确保在使用 API 时提供正确的参数。
对于模拟交易功能，请确认是否已启用模拟交易模式。
## 5. 版本历史
1.0.0: 初始化版本 (20240529)

