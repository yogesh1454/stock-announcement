"""
    Implements live data fetch functionality
"""
from datetime import datetime
from requests import Session
class NSELive:
    time_out = 5
    base_url = "https://www.nseindia.com/api"
    page_url = "https://www.nseindia.com/get-quotes/equity?symbol=LT"
    _routes = {
            "stock_meta": "/equity-meta-info",
            "stock_quote": "/quote-equity",
            "stock_derivative_quote": "/quote-derivative",
            "market_status": "/marketStatus",
            "chart_data": "/chart-databyindex",
            "market_turnover": "/market-turnover",
            "equity_derivative_turnover": "/equity-stock",
            "all_indices": "/allIndices",
            "live_index": "/equity-stockIndices",
            "index_option_chain": "/option-chain-indices",
            "equity_option_chain": "/option-chain-equities",
            "currency_option_chain": "/option-chain-currency",
            "pre_open_market": "/market-data-pre-open",
            "holiday_list": "/holiday-master?type=trading",
            "corporate_action": "/corporate-announcements?index=equities&from_date=30-01-2024&to_date=06-02-2024",
            "corporate-further-issues-ri": "/corporate-further-issues-ri?",
            "corporate-announcements": "/corporate-announcements",
    }

    def __init__(self):
        self.s = Session()
        h = {
            "Host": "www.nseindia.com",
            "Referer": "https://www.nseindia.com/get-quotes/equity?symbol=SBIN",
            "X-Requested-With": "XMLHttpRequest",
            "pragma": "no-cache",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            }
        self.s.headers.update(h)
        self.s.get(self.page_url)
        print("loading done")

    def download(self, url):
        return self.s.get(url)

    def corporate_announcements(self, index, from_dt):
        data = {'index':index, 'from_date':from_dt, 'to_date':from_dt}
        return self.get("corporate-announcements", data)


    def get(self, route, payload={}):
        url = self.base_url + self._routes[route]
        print("url: ", url ," ;params: ", payload)
        r = self.s.get(url, params=payload)
        print("### NSE Live RESPONSE STATUS: ", r)
        #print("### RESPONSE: ", r.json())
        return r.json()

    def corporate_action(self, symbol):
        data = {"symbol": symbol}
        return self.get("corporate_action", data)


    def corporate_further_issues_ri(self, symbol):
        data = {"symbol": symbol}
        return self.get("corporate_action", data)

    def stock_quote(self, symbol):
        data = {"symbol": symbol}
        return self.get("stock_quote", data)


    def stock_quote_fno(self, symbol):
        data = {"symbol": symbol}
        return self.get("stock_derivative_quote", data)


    def trade_info(self, symbol):
        data = {"symbol": symbol, "section": "trade_info"}
        return self.get("stock_quote", data)


    def market_status(self):
        return self.get("market_status", {})


    def chart_data(self, symbol, indices=False):
        data = {"index" : symbol + "EQN"}
        if indices:
            data["index"] = symbol
            data["indices"] = "true"
        return self.get("chart_data", data)


    def tick_data(self, symbol, indices=False):
        return self.chart_data(symbol, indices)


    def market_turnover(self):
        return self.get("market_turnover")


    def eq_derivative_turnover(self, type="allcontracts"):
        data = {"index": type}
        return self.get("equity_derivative_turnover", data)


    def all_indices(self):
        return self.get("all_indices")

    def live_index(self, symbol="NIFTY 50"):
        data = {"index" : symbol}
        return self.get("live_index", data)


    def index_option_chain(self, symbol="NIFTY"):
        data = {"symbol": symbol}
        return self.get("index_option_chain", data)


    def equities_option_chain(self, symbol):
        data = {"symbol": symbol}
        return self.get("equity_option_chain", data)


    def currency_option_chain(self, symbol="USDINR"):
        data = {"symbol": symbol}
        return self.get("currency_option_chain", data)


    def live_fno(self):
        return self.live_index("SECURITIES IN F&O")


    def pre_open_market(self, key="NIFTY"):
        data = {"key": key}
        return self.get("pre_open_market", data)


    def holiday_list(self):
        return self.get("holiday_list", {})
