import random


class GameBrain:
    def __init__(self):
        self.your_account_balance = 100
        self.stock_hold = 0

    def generate_current_per_stock_price(self):
        return random.randint(0, 100)

    def buy_stock(self, buy_number: int, current_per_stock_price: int):
        number_of_stock_to_buy = buy_number
        total_stock_price = number_of_stock_to_buy * current_per_stock_price

        if total_stock_price < self.your_account_balance:
            self.stock_hold = number_of_stock_to_buy
            self.your_account_balance -= total_stock_price
            balance_stock_tuple = (self.your_account_balance, self.stock_hold)
            return balance_stock_tuple
        elif total_stock_price > self.your_account_balance:
            balance_stock_tuple = (0, 0)
            return balance_stock_tuple

    def sell_stock(self, sell_number: int, current_per_stock_price: int):
        number_of_stock_to_sell = sell_number
        total_stock_price = number_of_stock_to_sell * current_per_stock_price

        if number_of_stock_to_sell <= self.stock_hold:
            self.stock_hold -= number_of_stock_to_sell
            self.your_account_balance += total_stock_price

            balance_stock_tuple = (self.your_account_balance, self.stock_hold)
            return balance_stock_tuple
        else:
            balance_stock_tuple = (0, 0)
            return balance_stock_tuple

