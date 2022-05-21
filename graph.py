import matplotlib.pyplot as plt

FONT_DICT = {
    'fontname': 'Comic Sans MS',
    'weight': 'normal',
    'size': 16,
}

# Toolbar remove
plt.rcParams['toolbar'] = 'None'

x_values = [1, 2, 3, 4, 5]
y_values = [30, 50, 85, 60, 50]

# graph resize
plt.figure(figsize=(5, 5))

plt.plot(x_values, y_values, color="green", marker=".", markersize="10")
plt.title("Stock Market", fontdict=FONT_DICT)
plt.xlabel("Days")
plt.ylabel("Prices")

plt.xticks([1, 2, 3, 4, 5])
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.show()
