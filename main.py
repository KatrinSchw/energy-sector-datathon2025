import matplotlib
matplotlib.use('TkAgg')

from weekly_gasoline_prices import (
    plot_gasoline_prices,
    plot_gasoline_prices_with_outages
)
from weekly_supply_estimates import (
    plot_gasoline_stocks,
    plot_gasoline_production,
    plot_refinery_utilization,
    plot_gross_inputs,
    plot_gasoline_imports,
    plot_gasoline_exports,
    plot_variable_with_outage,
)

if __name__ == '__main__':
    #plot_gasoline_prices()
    #plot_gasoline_stocks()
    # plot_gasoline_production()
    #plot_refinery_utilization()
    #plot_gross_inputs()
    # plot_gasoline_imports()
    # plot_gasoline_exports()
    plots = {
        'Weekly U.S. Ending Stocks of Total Gasoline  (Thousand Barrels)':
            ('Ending Stocks of Total Gasoline', 'navy'),
        'Weekly U.S. Refiner and Blender Net Production of Finished Motor Gasoline  (Thousand Barrels per Day)':
            ('Net Production of Finished Motor Gasoline', 'darkgreen'),
        'Weekly U.S. Percent Utilization of Refinery Operable Capacity (Percent)':
            ('Refinery Utilization Rate (%)', 'orange'),
        'Weekly U.S. Gross Inputs into Refineries  (Thousand Barrels per Day)':
            ('Gross Inputs into Refineries', 'crimson'),
        'Weekly U.S. Imports of Total Gasoline  (Thousand Barrels per Day)':
            ('Imports of Total Gasoline', 'purple'),
        'Weekly U.S. Exports of Total Motor Gasoline (Thousand Barrels per Day)':
            ('Exports of Total Motor Gasoline', 'brown'),
    }

    for column, (title, color) in plots.items():
        plot_variable_with_outage(
            column=column,
            title=title,
            color=color,
            outage_col='Marathon_Outage',
            outage_label='Marathon Refinery Fire (Aug 2023)'
        )

    plot_gasoline_prices_with_outages()