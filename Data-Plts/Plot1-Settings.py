import numpy as np
import pandas as pd
import matplotlib.pylab as plt 
from matplotlib.ticker import ScalarFormatter, StrMethodFormatter


df = pd.read_csv('List_of_countries_by_carbon_dioxide_emissions.csv')

x1 = df['Fossil CO2 emissions(Mt CO2)'][0]
x2 = df['Unnamed: 2'][0]
x3 = df['Unnamed: 3'][0]

y1 = df['Fossil CO2 emissions(Mt CO2)'][1]
y2 = df['Unnamed: 2'][1]
y3 = df['Unnamed: 3'][1]

bar_width = 5  # Width of the bars
bar_color = 'red'  # Color of the bars
edge_color = 'black'  # Color of the bar edges
bar_opacity = 0.75  # Opacity of the bars
bar_linewidth = 1  # Width of the bar edges

fig, ax = plt.subplots()

ax.bar(x1, y1, label=x1, width=bar_width, color=bar_color, edgecolor=edge_color,
        alpha=bar_opacity, linewidth=bar_linewidth)
ax.bar(x2, y2, label=x2,  width=bar_width, color=bar_color, edgecolor=edge_color,
        alpha=bar_opacity, linewidth=bar_linewidth)
ax.bar(x3, y3, label=x3,  width=bar_width, color=bar_color, edgecolor=edge_color,
        alpha=bar_opacity, linewidth=bar_linewidth)

ax.set_yscale('log')
ax.set_xticks(np.arange(1990, 2020, 3))

plt.gca().yaxis.set_major_formatter(ScalarFormatter()) 
plt.gca().yaxis.set_minor_formatter(ScalarFormatter());  

plt.xlabel('Year')
plt.ylabel('Co2 Emissions By Year')
plt.title('World Co2 Emissions In Mt')
plt.legend()

plt.savefig('co2_emissions_plot.png', dpi=300)

plt.show()
