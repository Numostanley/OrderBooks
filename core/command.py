from typing import Callable


class OrderBookCommand:
    def __init__(self, exchanges: list, quantity):
        self.exchanges: list[Callable] = exchanges
        self.quantity: int = quantity
    
    def run(self, aggregator: Callable, calculator: Callable) -> None:
        _aggregator = aggregator()
        bids, asks = _aggregator.merge_order_books(self.exchanges)

        buy_price, sell_price = calculator(
            bids=bids, asks=asks, quantity=self.quantity
        )
        print(f"Price to buy {self.quantity} bitcoins: ${buy_price:.2f}")
        print(f"Price to sell {self.quantity} bitcoins: ${sell_price:.2f}")