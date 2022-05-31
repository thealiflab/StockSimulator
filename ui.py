import tkinter
from game_brain import GameBrain
from tkinter import simpledialog, messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator

FONT = "arial"

x_list = [1]
y_list = [1]
drawn = 0


class GameUI:
    def __init__(self, game_brain: GameBrain):
        self.brain = game_brain
        self.window = tkinter.Tk()
        self.window.title("Stock Simulator - Rich in Days")
        self.window.config(padx=0, pady=0, bg="white")
        self.window.minsize(width=500, height=660)

        self.current_stock_value_text: int = 0
        self.user_input_data: int = 0

        # --------------- Matplotlib Graph --------------- #

        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.ax = self.fig.add_subplot(1, 1, 1)

        self.axis_draw()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(expand=True)

        # --------------- Matplotlib Graph End--------------- #

        # Day Value label
        # self.high_score_label = tkinter.Label(text="1", font=(FONT, 15), bg="white")
        # self.high_score_label.place(x=230, y=40)

        # Current Stock label
        self.current_stock_label = tkinter.Label(text="💰 Current Stock Price 💰")
        self.current_stock_label.config(font=(FONT, 13), fg="#4D77FF", bg="white")
        self.current_stock_label.place(x=30, y=10, width=225, height=70)

        # Current Stock Value label
        self.stock_price_value = tkinter.Label(text="", bg="white")
        self.stock_price_value.place(x=100, y=65, width=70, height=25)

        # Sell button
        self.sell_button = tkinter.Button(text="Sell ⬆", bg="#F55353", fg="white", command=self.sell_button_pressed)
        self.sell_button.place(x=90, y=580, width=70, height=40)

        # Day Plus button
        self.day_button = tkinter.Button(text="➕ Day ➕", bg="#30AADD", fg="white", command=self.day_button_pressed)
        self.day_button.place(x=220, y=570, width=70, height=60)

        # Buy button
        self.buy_button = tkinter.Button(text="Buy ⬇", bg="#14C38E", fg="white", command=self.buy_button_pressed)
        self.buy_button.place(x=350, y=580, width=70, height=40)

        # Account Balance label
        self.account_balance_label = tkinter.Label(text="Account Balance:", font=(FONT, 13), bg="white")
        self.account_balance_label.place(x=260, y=30, width=182, height=30)

        # Account Balance Value label
        self.account_balance_value_label = tkinter.Label(text="100", font=(FONT, 13), bg="white")
        self.account_balance_value_label.place(x=420, y=33)

        # Stock Onhold label
        self.stock_hold_label = tkinter.Label(text="Stock hold:", font=(FONT, 13), bg="white")
        self.stock_hold_label.place(x=308, y=60, width=133, height=30)

        # Stock Onhold Value label
        self.stock_hold_value_label = tkinter.Label(text="0", font=(FONT, 13), bg="white")
        self.stock_hold_value_label.place(x=420, y=63)

        # To generate first random current per stock value
        self.day_button_pressed()

        self.window.mainloop()

    def axis_draw(self):
        self.ax.clear()
        self.ax.set(xlabel='', ylabel='Price')
        global drawn
        drawn += 1

        self.ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        self.ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        self.ax.plot(x_list, y_list, "green")

        if drawn > 11:
            self.ax.set_xticks(range(0, drawn))
        else:
            self.ax.set_xticks(range(0, 11))

        self.ax.set_yticks(range(0, 101, 10))

    def sell_button_pressed(self):

        bid_text = self.user_input_popup()
        got_balance_stock_tuple = self.brain.sell_stock(
            sell_number=bid_text,
            current_per_stock_price=self.current_stock_value_text
        )
        self.update_balance_stock_value_label(got_balance_stock_tuple)

    def day_button_pressed(self):

        self.current_stock_value_text = self.brain.generate_current_per_stock_price()
        print(self.current_stock_value_text)
        self.stock_price_value.config(text=self.current_stock_value_text, fg="#4D77FF", font=(FONT, 18))

        # ------------------ Graph Section ------------------
        x_list.append(x_list[-1] + 1)
        y_list.append(self.current_stock_value_text)

        self.axis_draw()

        self.canvas.draw()  # redraw

        print(x_list)
        print(y_list)

    def buy_button_pressed(self):

        bid_text = self.user_input_popup()
        got_balance_stock_tuple = self.brain.buy_stock(
            buy_number=bid_text,
            current_per_stock_price=self.current_stock_value_text
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
            if self.user_input_data >= 0:
                return self.user_input_data
            else:
                return self.user_input_popup()
        else:
            return 0
