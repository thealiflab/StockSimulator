import tkinter
from game_brain import GameBrain
from tkinter import simpledialog, messagebox

FONT = "arial"


class GameUI:
    def __init__(self, game_brain: GameBrain):
        self.brain = game_brain
        self.window = tkinter.Tk()
        self.window.title("Stock Simulator - Rich in 10 Days")
        self.window.config(padx=20, pady=20, bg="white")
        self.window.minsize(width=450, height=471)

        self.current_stock_text = 0
        self.user_input_data: int = 0

        # Day Indicator
        self.high_score_label = tkinter.Label(text="Day 1")
        self.high_score_label.config(font=(FONT, 15), bg="white")
        self.high_score_label.place(x=170, y=40, width=98, height=30)

        # Current Stock Value label
        self.current_stock_label = tkinter.Label(text="Current Per Stock Price:")
        self.current_stock_label.config(font=(FONT, 13), bg="white")
        self.current_stock_label.place(x=110, y=80, width=225, height=79)

        # Current Stock Value label
        self.per_price_label = tkinter.Label(text="", bg="white")
        self.per_price_label.place(x=170, y=180, width=70, height=25)

        # Sell button
        self.sell_button = tkinter.Button(text="Sell ⬆", bg="#F55353", fg="white", command=self.sell_button_pressed)
        self.sell_button.place(x=50, y=270, width=70, height=40)

        # Day Plus button
        self.day_button = tkinter.Button(text="➕ Day ➕", bg="#30AADD", fg="white", command=self.day_button_pressed)
        self.day_button.place(x=180, y=260, width=70, height=60)

        # Buy button
        self.buy_button = tkinter.Button(text="Buy ⬇", bg="#14C38E", fg="white", command=self.buy_button_pressed)
        self.buy_button.place(x=310, y=270, width=70, height=40)

        # Account Balance label
        self.account_balance_label = tkinter.Label(text="Account Balance:", font=(FONT, 13), bg="white")
        self.account_balance_label.place(x=50, y=360, width=182, height=30)

        # Account Balance Value label
        self.account_balance_value_label = tkinter.Label(text="100", font=(FONT, 13), bg="white")
        self.account_balance_value_label.place(x=210, y=362)

        # Stock Onhold label
        self.stock_hold_label = tkinter.Label(text="Stock hold:", font=(FONT, 13), bg="white")
        self.stock_hold_label.place(x=50, y=390, width=133, height=30)

        # Stock Onhold Value label
        self.stock_hold_value_label = tkinter.Label(text="0", font=(FONT, 13), bg="white")
        self.stock_hold_value_label.place(x=160, y=392)

        self.day_button_pressed()

        self.window.mainloop()

    def sell_button_pressed(self):
        bid_text = self.user_input_popup()
        got_balance_stock_tuple = self.brain.sell_stock(
            sell_number=bid_text,
            current_per_stock_price=self.current_stock_text
        )
        self.update_balance_stock_value_label(got_balance_stock_tuple)

    def day_button_pressed(self):
        self.current_stock_text = self.brain.generate_current_per_stock_price()
        self.current_stock_label.config(text=self.current_stock_text, fg="#4D77FF", font=(FONT, 25))

    def buy_button_pressed(self):
        bid_text = self.user_input_popup()
        got_balance_stock_tuple = self.brain.buy_stock(
            buy_number=bid_text,
            current_per_stock_price=self.current_stock_text
        )
        self.update_balance_stock_value_label(got_balance_stock_tuple)

    def update_balance_stock_value_label(self, balance_stock_tuple: tuple):
        if balance_stock_tuple == (0, 0):
            tkinter.messagebox.showerror(
                title="Insufficient balance!",
                message="Please try again! You have insufficient amount"
            )
        else:
            self.account_balance_value_label.config(text=balance_stock_tuple[0])
            self.stock_hold_value_label.config(text=balance_stock_tuple[1])

    def user_input_popup(self):
        self.user_input_data = simpledialog.askinteger(
            title="Bid",
            prompt="How many stock you want to buy/sell:"
        )

        if self.user_input_data is not None:
            return self.user_input_data
        else:
            self.user_input_popup()
