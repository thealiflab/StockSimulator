import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random

window = tkinter.Tk()
window.title("Matplotlib in Tkinter")
window.minsize(640, 400)

n = random.randint(0, 100)
x_list = [1]
y_list = [3]


def graph_extend():
    x_list.append(random.randint(1, 10))
    y_list.append(random.randint(1, 10))

    ax.clear()
    ax.plot(x_list, y_list)  # inform matplotlib of the new data
    canvas.draw()  # redraw

    print(x_list)
    print(y_list)


fig = Figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(1, 1, 1)
ax.plot(x_list, y_list)

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(expand=True)

button = tkinter.Button(text="Extend", command=graph_extend)
button.pack()

tkinter.mainloop()
