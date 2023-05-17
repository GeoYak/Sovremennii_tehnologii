class CoinHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, coin):
        if self.next_handler:
            return self.next_handler.handle(coin)


class OneCoinHandler(CoinHandler):
    def handle(self, coin):
        if coin == 1:
            return {1: 1}
        else:
            return super().handle(coin)


class FiveCoinHandler(CoinHandler):
    def handle(self, coin):
        if coin == 5:
            return {5: 1}
        else:
            return super().handle(coin)


class TenCoinHandler(CoinHandler):
    def handle(self, coin):
        if coin == 10:
            return {10: 1}
        else:
            return super().handle(coin)


class TwentyFiveCoinHandler(CoinHandler):
    def handle(self, coin):
        if coin == 25:
            return {25: 1}
        else:
            return super().handle(coin)


class CoinProcessor:
    def __init__(self):
        self.handlers = OneCoinHandler(FiveCoinHandler(TenCoinHandler(TwentyFiveCoinHandler())))
        self.total_amount = 0
        self.coins_count = {1: 0, 5: 0, 10: 0, 25: 0}

    def add_coin(self, coin):
        result = self.handlers.handle(coin)
        if result:
            amount = list(result.keys())[0]
            self.total_amount += amount
            self.coins_count[amount] += 1

    def print_total_amount(self):
        print("Total amount:", self.total_amount)
        print("Coins count:")
        for coin, count in self.coins_count.items():
            print(f"{coin}: {count}")


processor = CoinProcessor()
processor.add_coin(1)
processor.add_coin(5)
processor.add_coin(10)
processor.add_coin(25)
processor.add_coin(25)

processor.print_total_amount()
