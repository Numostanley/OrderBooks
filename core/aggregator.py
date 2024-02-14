from typing import Callable


class OrderBookAggregator:
    def __init__(self):
        self.merged_order_book: dict[str, list] = {'bids': [], 'asks': []}

    @staticmethod
    def fetch_order_book(exchange: Callable) -> dict:
        order_book: dict = exchange()
        return order_book

    def merge_order_books(self, exchanges: list[Callable]) -> tuple[list[list], list[list]]:
        for exchange in exchanges:
            order_book: dict = self.fetch_order_book(exchange)
            bids: list[tuple] = order_book['bids']
            asks: list[tuple] = order_book['asks']
            self.merged_order_book['bids'].extend(bids)
            self.merged_order_book['asks'].extend(asks)

        # Sort the merged bids and asks
        self.merged_order_book['bids'].sort(key=lambda x: float(x[0]), reverse=True)
        self.merged_order_book['asks'].sort(key=lambda x: float(x[0]))

        return self.merged_order_book['bids'], self.merged_order_book['asks']
