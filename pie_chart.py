import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('shopping_behavior_updated.csv')
size_group = df.groupby('Category')['Purchase Amount (USD)'].sum()
size_group = size_group.sort_values()

plt.figure(figsize=(6, 6))
plt.pie(
    size_group,
    labels=size_group.index,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'edgecolor': 'black'}
)

plt.title('Distribución del gasto por categoría', fontsize=14, weight='bold')
plt.show()