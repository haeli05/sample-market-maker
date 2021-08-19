import sys

from market_maker.market_maker import OrderManager


class CustomOrderManager(OrderManager):
    """A sample order manager for implementing your own custom strategy"""

    def place_orders(self) -> None:
        # implement your custom strategy here



        ## Pull books and quote

        # Define instruments on Bitmex.com
        #Perp = XBTUSD
        #Sep = XBTU21
        #DEC = XBTZ21

        # Perp_Ticker = self.get_ticker(XBTUSD)
        # print('Perp Ticker:')
        # print(Perp_Ticker)
        # print()

        # Future_Ticker = self.get_ticker(XBTZ21)
        # print('Future Ticker')
        # print(Future_Ticker)
        # print()






        buy_orders = []
        sell_orders = []



        # populate buy and sell orders, e.g.
        # buy_orders.append({'price': 999.0, 'orderQty': 100, 'side': "Buy"})
        # sell_orders.append({'price': 1001.0, 'orderQty': 100, 'side': "Sell"})

        self.converge_orders(buy_orders, sell_orders)


    def checkSpread(self, tickers) -> None:
        #return spread of the two tickers, first being the base


            return (tickers[1] - tickers[0])/tickers[0]

def run() -> None:
    order_manager = CustomOrderManager()

    # Try/except just keeps ctrl-c from printing an ugly stacktrace
    try:
        order_manager.run_loop()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
