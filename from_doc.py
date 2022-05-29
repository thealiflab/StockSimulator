import tkinter
import random

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy


root = tkinter.Tk()
root.wm_title("Stock Market")

fig = Figure(figsize=(6, 4), dpi=100)
t = numpy.arange(0, 4, 1)
ax = fig.add_subplot()
line = ax.plot(t, 2 * numpy.sin(2 * numpy.pi * t))
ax.set_xlabel("Days")
ax.set_ylabel("Prices")

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

# pack_toolbar=False will make it easier to use a layout manager later on.
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

canvas.mpl_connect(
    "key_press_event", lambda event: print(f"you pressed {event.key}"))

#keypress handle kore
canvas.mpl_connect("key_press_event", key_press_handler)

button_quit = tkinter.Button(master=root, text="Quit", command=root.quit)


def update_frequency():
    # update data
    y = random.randint(0, 100)
    line.set_data(t, y)

    # required to update canvas and attached toolbar!
    canvas.draw()


random_y_update_button = tkinter.Button(root, text="Updated", command=update_frequency)

# Packing order is important. Widgets are processed sequentially and if there
# is no space left, because the window is too small, they are not displayed.
# The canvas is rather flexible in its size, so we pack it last which makes
# sure the UI controls are displayed as long as possible.
button_quit.pack(side=tkinter.BOTTOM)
random_y_update_button.pack(side=tkinter.BOTTOM)
toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()
