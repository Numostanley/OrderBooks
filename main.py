import time
from decimal import Decimal, InvalidOperation

from core import exchange, aggregator, command, calculator


def main():
    exchanges = [exchange.coinbase, exchange.gemini, exchange.kraken]
    try:
        quantity: Decimal = Decimal(input("Please input your desired quantity (Default = 10): "))
    except InvalidOperation:
        quantity: Decimal = Decimal(10)

    start_time = time.time()
    try:
        program = command.OrderBookCommand(
            exchanges=exchanges,
            quantity=quantity
        )
        program.run(
            aggregator=aggregator.OrderBookAggregator,
            calculator=calculator.price_calculator
        )
    except Exception as error:
        print(error)

    end_time = time.time()
    print("Executed in:", round(end_time - start_time, 2), "seconds")


if __name__ == "__main__":
    main()
