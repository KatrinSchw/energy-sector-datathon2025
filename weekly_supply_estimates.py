import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt

def load_supply_data():
    df = pd.read_csv("datasets/weekly_supply_estimates.csv")
    df['Date'] = pd.to_datetime(df['Date'], format="%b %d, %Y")

    outage_start = pd.to_datetime("2023-08-25")
    outage_end = pd.to_datetime("2023-10-06")
    df['Marathon_Outage'] = df['Date'].between(outage_start, outage_end)

    df = df.sort_values('Date')
    return df

def plot_variable_with_outage(column, title, color, outage_col, outage_label):
    df = load_supply_data()
    df = df[df['Date'] >= pd.to_datetime("2020-01-01")]
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df[column], color=color, linewidth=2, label=title)

    outage = df[df[outage_col]]
    if not outage.empty:
        plt.axvspan(outage['Date'].min(), outage['Date'].max(), color='red', alpha=0.2, label=outage_label)
    else:
        print(f"No data for the specified outage period: {outage_label}")

    plt.title(f'{title} ( {outage_label})', fontsize=14)
    plt.xlabel('Date')
    plt.ylabel(column.split("(")[0].strip())
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


#Ending Stocks of Total Gasoline (Inventory Levels)
def plot_gasoline_stocks():
    df = load_supply_data()
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Weekly U.S. Ending Stocks of Total Gasoline  (Thousand Barrels)'], color='navy', linewidth=2)
    plt.title('Weekly U.S. Ending Stocks of Total Gasoline', fontsize=14)
    plt.xlabel('Date')
    plt.ylabel('Thousand Barrels')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#Net Production of Finished Motor Gasoline
def plot_gasoline_production():
    df = load_supply_data()
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Weekly U.S. Refiner and Blender Net Production of Finished Motor Gasoline  (Thousand Barrels per Day)'], color='darkgreen', linewidth=2)
    plt.title('Net Production of Finished Motor Gasoline', fontsize=14)
    plt.xlabel('Date')
    plt.ylabel('Thousand Barrels/Day')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#Percent Utilization of Refinery Operable Capacity
def plot_refinery_utilization():
    df = load_supply_data()
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Weekly U.S. Percent Utilization of Refinery Operable Capacity (Percent)'], color='orange', linewidth=2)
    plt.title('Refinery Operable Capacity Utilization (%)', fontsize=14)
    plt.xlabel('Date')
    plt.ylabel('Percent')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#Gross Inputs into Refineries
def plot_gross_inputs():
    df = load_supply_data()
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Weekly U.S. Gross Inputs into Refineries  (Thousand Barrels per Day)'], color='crimson', linewidth=2)
    plt.title('Gross Inputs into Refineries', fontsize=14)
    plt.xlabel('Date')
    plt.ylabel('Thousand Barrels/Day')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#Imports of Total Gasoline
def plot_gasoline_imports():
    df = load_supply_data()
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Weekly U.S. Imports of Total Gasoline  (Thousand Barrels per Day)'], color='purple', linewidth=2)
    plt.title('Imports of Total Gasoline', fontsize=14)
    plt.xlabel('Date')
    plt.ylabel('Thousand Barrels/Day')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#Exports of Total Gasoline
def plot_gasoline_exports():
    df = load_supply_data()
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Weekly U.S. Exports of Total Motor Gasoline (Thousand Barrels per Day)'], color='brown', linewidth=2)
    plt.title('Exports of Total Motor Gasoline', fontsize=14)
    plt.xlabel('Date')
    plt.ylabel('Thousand Barrels/Day')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

