from decimal import Decimal


def price_calculator(bids: list[list], asks: list[list], quantity: int) -> tuple[Decimal, Decimal]:
    buy_price = 0
    sell_price = 0

    # Calculate the price to buy the specified quantity
    buy_quantity: int = quantity
    for bid in bids:
        price, amount, _ = bid
        amount = Decimal(amount)
        if buy_quantity <= 0:
            break
        if buy_quantity <= amount:
            buy_price += buy_quantity * Decimal(price)
            buy_quantity = 0
        else:
            buy_price += amount * Decimal(price)
            buy_quantity -= amount

    # Calculate the price to sell the specified quantity
    sell_quantity: int = quantity
    for ask in asks:
        price, amount, _ = ask
        amount = Decimal(amount)
        if sell_quantity <= 0:
            break
        if sell_quantity <= amount:
            sell_price += sell_quantity * Decimal(price)
            sell_quantity = 0
        else:
            sell_price += amount * Decimal(price)
            sell_quantity -= amount

    return Decimal(buy_price), Decimal(sell_price)
