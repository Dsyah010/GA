import matplotlib.pyplot as plt
from itertools import permutations, combinations
from random import shuffle
import random
import numpy as np
import statistics
import pandas as pd
import seaborn as sns

x = [1,3,5,7,10,18,16,11,8,1.5]
y = [0,2,1,4.5,-1,2.5,10,6,7,10]
cities_names = ["Kota Bharu", "Jeli", "Tanah Merah", "Kuala Krai", "Pasir Mas", "Pasir Puteh", "Machang", "Tumpat", "Lojing", "Bachok"]
city_coords = dict(zip(cities_names, zip(x, y)))
n_population = 250
crossover_per = 0.8
mutation_per = 0.2
n_generations = 200

# Pastel Pallete
colors = sns.color_palette("pastel", len(cities_names))

# City Icons
city_icons = {
    "Kota Bharu": "♕",
    "Jeli": "♖",
    "Tanah Merah": "♗",
    "Kuala Krai": "♘",
    "Pasir Mas": "♙",
    "Pasir Puteh": "♔",
    "Machang": "♚",
    "Tumpat": "♛",
    "Lojing": "♜",
    "Bachok": "♝"
}

fig, ax = plt.subplots()

ax.grid(False)  # Grid

for i, (city, (city_x, city_y)) in enumerate(city_coords.items()):
    color = colors[i]
    icon = city_icons[city]
    ax.scatter(city_x, city_y, c=[color], s=1200, zorder=2)
    ax.annotate(icon, (city_x, city_y), fontsize=40, ha='center', va='center', zorder=3)
    ax.annotate(city, (city_x, city_y), fontsize=12, ha='center', va='bottom', xytext=(0, -30),
                textcoords='offset points')

    # Connect cities with opaque lines
    for j, (other_city, (other_x, other_y)) in enumerate(city_coords.items()):
        if i != j:
            ax.plot([city_x, other_x], [city_y, other_y], color='gray', linestyle='-', linewidth=1, alpha=0.1)

fig.set_size_inches(16, 12)
plt.show()
