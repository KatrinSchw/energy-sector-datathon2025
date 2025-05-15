import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt

def plot_gasoline_prices():
    df = pd.read_csv("datasets/weekly_gasoline_prices.csv")

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


def plot_gasoline_prices_with_outages():
    df = pd.read_csv("datasets/weekly_gasoline_prices.csv")
    df['Date'] = pd.to_datetime(df['Date'], format="%b %d, %Y")
    df = df[df['Date'] >= pd.to_datetime("2020-01-01")]
    df = df.sort_values('Date')

    outage_start = pd.to_datetime("2023-08-25")
    outage_end = pd.to_datetime("2023-10-06")

    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Price'], color='darkorange', linewidth=2, label='Gasoline Price')

    plt.axvspan(outage_start, outage_end, color='red', alpha=0.2, label='Marathon Refinery Fire (Aug 2023)')

    plt.title('Weekly US Gasoline Prices (2020–2023)', fontsize=14)
    plt.xlabel('Date')
    plt.ylabel('Price (USD per Gallon)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()