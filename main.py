import random

is_game_on = True

your_account_balance = 100
stock_hold = 0
rounds = 1


def want_to_trade():
    answer = input("Do you want to trade at this price? Type yes or no: ").lower()
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        print("Invalid input!")
        want_to_trade()


def want_to_buy():
    answer = input("Do you want to buy stock or sell stock? Type buy or sell: ").lower()
    if answer == "buy":
        return True
    elif answer == "sell":
        return False
    else:
        print("Invalid input!")
        want_to_buy()


while is_game_on:
    print("=====================================================")

    # Generating new per stock price
    current_per_stock_price = random.randint(0, 101)

    if rounds == 6:
        is_game_on = False
    else:
        print(f"Your available balance: {your_account_balance}")
        print(f"Your stock: {stock_hold}")
        print(f"Rounds: {rounds}/5")
        print(f"\nCurrently Per Stock Price: {current_per_stock_price}\n")

        if want_to_trade():
            if want_to_buy():
                number_of_stock_to_buy = int(input("How many stocks you want to buy: "))
                total_stock_price = number_of_stock_to_buy * current_per_stock_price

                if total_stock_price < your_account_balance:
                    stock_hold = number_of_stock_to_buy
                    your_account_balance -= total_stock_price
                elif total_stock_price > your_account_balance:
                    print("Insufficient Balance! try to buy from your balance!!")
            else:
                number_of_stock_to_sell = int(input("How many stocks you want to sell: "))
                total_stock_price = number_of_stock_to_sell * current_per_stock_price

                if number_of_stock_to_sell > stock_hold:
                    print("Insufficient Stock! try to sell from your total stock!!")
                else:
                    stock_hold -= number_of_stock_to_sell
                    your_account_balance += total_stock_price
        rounds += 1


print(f"You have earned {your_account_balance - 100} in 5 rounds")
