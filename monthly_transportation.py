import pandas as pd
import matplotlib.pyplot as plt

def plot_vehicle_miles():
    df = pd.read_csv("datasets/monthly_transportation_statistics.csv")

    df['Date'] = pd.to_datetime(df['Date'], format="%m/%d/%Y %I:%M:%S %p")

    plt.figure(figsize=(14, 6))
    plt.plot(df['Date'], df['Highway Vehicle Miles Traveled - All Systems'], label='Total', linewidth=2)
    plt.plot(df['Date'], df['Highway Vehicle Miles Traveled - Total Rural'], label='Rural', linestyle='--')
    plt.plot(df['Date'], df['Highway Vehicle Miles Traveled - Rural Interstate'], label='Rural Interstate',
             linestyle=':')

    plt.title('Monthly Vehicle Miles Traveled', fontsize=14)
    plt.xlabel('Date')
    plt.ylabel('Vehicle Miles Traveled')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_gasoline_prices_vs_vehicle_miles():
    gas_df = pd.read_csv("datasets/weekly_gasoline_prices.csv")
    gas_df['Date'] = pd.to_datetime(gas_df['Date'], format="%b %d, %Y")
    gas_df = gas_df.set_index('Date')
    gas_monthly = gas_df['Price'].resample('ME').mean().reset_index()
    gas_monthly.rename(columns={'Price': 'Avg Gasoline Price'}, inplace=True)

    vmt_df = pd.read_csv("datasets/monthly_transportation_statistics.csv")
    vmt_df['Date'] = pd.to_datetime(vmt_df['Date'], format="%m/%d/%Y %I:%M:%S %p")
    vmt_df = vmt_df[['Date', 'Highway Vehicle Miles Traveled - All Systems']]
    vmt_df.rename(columns={'Highway Vehicle Miles Traveled - All Systems': 'Total VMT'}, inplace=True)

    vmt_df['Date'] = vmt_df['Date'].dt.to_period('M').dt.to_timestamp('M')
    gas_monthly['Date'] = gas_monthly['Date'].dt.to_period('M').dt.to_timestamp('M')

    vmt_df['Total VMT'] = pd.to_numeric(vmt_df['Total VMT'], errors='coerce')
    gas_monthly['Avg Gasoline Price'] = pd.to_numeric(gas_monthly['Avg Gasoline Price'], errors='coerce')

    min_date = max(vmt_df['Date'].min(), gas_monthly['Date'].min())
    max_date = min(vmt_df['Date'].max(), gas_monthly['Date'].max())
    vmt_df = vmt_df[(vmt_df['Date'] >= min_date) & (vmt_df['Date'] <= max_date)]
    gas_monthly = gas_monthly[(gas_monthly['Date'] >= min_date) & (gas_monthly['Date'] <= max_date)]

    merged = pd.merge(vmt_df, gas_monthly, on='Date', how='inner')
    merged = merged.dropna(subset=['Total VMT', 'Avg Gasoline Price'])
    fig, ax1 = plt.subplots(figsize=(14, 6))

    ax1.set_title("Monthly Gasoline Price vs. Total Vehicle Miles Traveled", fontsize=14)
    ax1.set_xlabel("Date")

    ax1.plot(merged['Date'], merged['Total VMT'], color='blue', linewidth=2)
    ax1.set_ylabel("Total Vehicle Miles Traveled", color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(merged['Date'], merged['Avg Gasoline Price'], color='orange', linewidth=2)
    ax2.set_ylabel("Gasoline Price (USD per Gallon)", color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')

    fig.tight_layout()
    plt.grid(True)
    plt.show()


def plot_transit_ridership():
    df = pd.read_csv("datasets/monthly_transportation_statistics.csv")

    df['Date'] = pd.to_datetime(df['Date'], format="%m/%d/%Y %I:%M:%S %p")

    df = df[df['Date'] >= pd.to_datetime("2015-01-01")]

    plt.figure(figsize=(14, 6))
    plt.plot(df['Date'], df['Transit Ridership - Urban Rail - Adjusted'], label='Urban Rail', color='green')
    plt.plot(df['Date'], df['Transit Ridership - Fixed Route Bus - Adjusted'], label='Fixed Route Bus', color='blue', linestyle='--')

    plt.title("Monthly Transit Ridership – Urban Rail vs Fixed Route Bus", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Monthly Riders (Adjusted)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_transit_ridership_vs_gasoline_prices():
    df = pd.read_csv("datasets/monthly_transportation_statistics.csv")
    df['Date'] = pd.to_datetime(df['Date'], format="%m/%d/%Y %I:%M:%S %p")
    df = df[['Date',
             'Transit Ridership - Urban Rail - Adjusted',
             'Transit Ridership - Fixed Route Bus - Adjusted']]

    df = df[df['Date'] >= pd.to_datetime("2015-01-01")]

    gas_df = pd.read_csv("datasets/weekly_gasoline_prices.csv")
    gas_df['Date'] = pd.to_datetime(gas_df['Date'], format="%b %d, %Y")
    gas_df = gas_df.set_index('Date')
    gas_monthly = gas_df['Price'].resample('ME').mean().reset_index()
    gas_monthly.rename(columns={'Price': 'Avg Gasoline Price'}, inplace=True)

    df['Date'] = df['Date'].dt.to_period('M').dt.to_timestamp('M')
    gas_monthly['Date'] = gas_monthly['Date'].dt.to_period('M').dt.to_timestamp('M')

    merged = pd.merge(df, gas_monthly, on='Date', how='inner')

    fig, ax1 = plt.subplots(figsize=(14, 6))

    ax1.plot(merged['Date'], merged['Transit Ridership - Urban Rail - Adjusted'],
             label='Urban Rail', color='green')
    ax1.plot(merged['Date'], merged['Transit Ridership - Fixed Route Bus - Adjusted'],
             label='Fixed Route Bus', color='blue', linestyle='--')
    ax1.set_ylabel("Monthly Transit Ridership", color='black')
    ax1.tick_params(axis='y', labelcolor='black')

    ax2 = ax1.twinx()
    ax2.plot(merged['Date'], merged['Avg Gasoline Price'],
             label='Avg Gasoline Price', color='orange', linewidth=2)
    ax2.set_ylabel("Gasoline Price (USD per Gallon)", color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')

    ax1.set_title("Transit Ridership vs. Gasoline Prices (2015–2023)", fontsize=14)
    ax1.set_xlabel("Date")
    ax1.grid(True)

    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc='upper left')

    plt.tight_layout()
    plt.show()