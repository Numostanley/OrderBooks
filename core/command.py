from typing import Callable
from decimal import Decimal


class OrderBookCommand:
    def __init__(self, exchanges: list, quantity: Decimal):
        self.exchanges: list[Callable] = exchanges
        self.quantity: Decimal = quantity
    
    def run(self, aggregator: Callable, calculator: Callable) -> None:
        _aggregator = aggregator()
        bids, asks = _aggregator.merge_order_books(self.exchanges)

        _calculator = calculator(
            bids=bids, asks=asks, quantity=self.quantity
        )
        buy_price, sell_price = _calculator.calculate()

        print(f"Price to buy {self.quantity} bitcoins: ${buy_price:.2f}")
        print(f"Price to sell {self.quantity} bitcoins: ${sell_price:.2f}")
