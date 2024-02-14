from decimal import Decimal


class PriceCalculator:
    def __init__(self, bids: list[list], asks: list[list], quantity: Decimal) -> None:
        self.bids = bids
        self.asks = asks
        self.quantity = quantity

    def calculate(self) -> tuple[Decimal, Decimal]:
        buy_price = Decimal(0)
        sell_price = Decimal(0)

        # Calculate the price to buy the specified quantity
        buy_quantity: Decimal = self.quantity
        for bid in self.bids:
            price, amount, _ = bid
            amount = Decimal(amount)
            if buy_quantity <= 0:
                break
            if buy_quantity <= amount:
                buy_price += buy_quantity * Decimal(price)
                buy_quantity = Decimal(0)
            else:
                buy_price += amount * Decimal(price)
                buy_quantity -= amount

        # Calculate the price to sell the specified quantity
        sell_quantity: Decimal = self.quantity
        for ask in self.asks:
            price, amount, _ = ask
            amount = Decimal(amount)
            if sell_quantity <= 0:
                break
            if sell_quantity <= amount:
                sell_price += sell_quantity * Decimal(price)
                sell_quantity = Decimal(0)
            else:
                sell_price += amount * Decimal(price)
                sell_quantity -= amount

        return Decimal(buy_price), Decimal(sell_price)
