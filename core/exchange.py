import os

import requests
import dotenv

dotenv.load_dotenv()


class Exchanges:
    COINBASE_URL = os.getenv("COINBASE_URL")
    GEMINI_URL = os.getenv("GEMINI_URL")

    def coinbase(self) -> dict:
        url: str = self.COINBASE_URL
        response: requests.Response = requests.get(url)
        order_book: dict = response.json()
        return order_book

    def gemini(self) -> dict:
        url: str = self.GEMINI_URL
        response: requests.Response = requests.get(url)
        order_book: dict = response.json()

        # reorganize data structure for aggregation
        new_order_book: dict = {}
        asks: list[list] = [[ask["price"], ask["amount"], ask["timestamp"]] for ask in order_book["asks"]]
        bids: list[list] = [[bid["price"], bid["amount"], bid["timestamp"]] for bid in order_book["bids"]]

        new_order_book.update({
            "asks": asks,
            "bids": bids
        })
        return new_order_book
