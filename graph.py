import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator
import random

window = tkinter.Tk()
window.title("Matplotlib in Tkinter")
window.minsize(640, 400)


x_list = [1]
y_list = [1]

def axis_draw():
    ax.clear()

    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.plot(x_list, y_list)

    ax.set_xticks(range(0, 11))
    ax.set_yticks(range(0, 11))

def graph_extend():
    x_list.append(x_list[-1]+1)
    y_list.append(random.randint(1, 10))

    axis_draw()

    canvas.draw()  # redraw

    print(x_list)
    print(y_list)


fig = Figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(1, 1, 1)
ax.set(xlabel='Day', ylabel='Price')

axis_draw()

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(expand=True)

button = tkinter.Button(text="Extend", command=graph_extend)
button.pack()

tkinter.mainloop()
