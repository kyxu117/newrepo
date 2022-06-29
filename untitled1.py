import yfinance as yf
stock = yf.Ticker('GOOG')
# 取得各種資料
#print(stock.info) # 取得公司資料
print(stock.financials) # 取得損益表
stock.balance_sheet # 取得資產負債表
stock.cashflow # 取得現金流量表
stock.history # 取得價量資料＋股利發放資料＋股票分割資料
