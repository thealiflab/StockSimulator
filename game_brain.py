import random


class GameBrain:
    def __init__(self):
        self.your_account_balance = 100
        self.stock_hold = 0
        self.current_per_stock_price = 0

    def generate_current_per_stock_price(self):
        self.current_per_stock_price = random.randint(0, 101)

    def want_to_trade(self):
        answer = input("Do you want to trade at this price? Type yes or no: ").lower()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Invalid input!")
            self.want_to_trade()

    def want_to_buy(self):
        answer = input("Do you want to buy stock or sell stock? Type buy or sell: ").lower()
        if answer == "buy":
            return True
        elif answer == "sell":
            return False
        else:
            print("Invalid input!")
            self.want_to_buy()

    def buy_stock(self):
        number_of_stock_to_buy = int(input("How many stocks you want to buy: "))
        total_stock_price = number_of_stock_to_buy * self.current_per_stock_price

        if total_stock_price < self.your_account_balance:
            self.stock_hold = number_of_stock_to_buy
            self.your_account_balance -= total_stock_price
        elif total_stock_price > self.your_account_balance:
            print("Insufficient Balance! try to buy from your balance!!")

    def sell_stock(self):
        number_of_stock_to_sell = int(input("How many stocks you want to sell: "))
        total_stock_price = number_of_stock_to_sell * self.current_per_stock_price

        if number_of_stock_to_sell > self.stock_hold:
            print("Insufficient Stock! try to sell from your total stock!!")
        else:
            self.stock_hold -= number_of_stock_to_sell
            self.your_account_balance += total_stock_price

    def simulate(self):
        self.generate_current_per_stock_price()

        print(f"Your available balance: {self.your_account_balance}")
        print(f"Your stock: {self.stock_hold}")
        print(f"\nCurrently Per Stock Price: {self.current_per_stock_price}\n")

        if self.want_to_trade():
            if self.want_to_buy():
                self.buy_stock()
            else:
                self.sell_stock()

    def result(self):
        print(f"You have earned {self.your_account_balance} in 5 rounds")
