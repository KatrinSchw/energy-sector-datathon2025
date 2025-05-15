import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt

def plot_gasoline_prices():
    df = pd.read_csv("weekly_gasoline_prices.csv")

    df['Date'] = pd.to_datetime(df['Date'], format="%b %d, %Y")

    df = df.sort_values('Date')

    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Price'], color='darkorange', linewidth=2)
    plt.title('Weekly US Gasoline Prices (2000+)', fontsize=14)
    plt.xlabel('Date')
    plt.ylabel('Price (USD per Gallon)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    plot_gasoline_prices()