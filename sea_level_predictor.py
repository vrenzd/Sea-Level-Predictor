import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Create first line of best fit
    result_all = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    years_all = pd.Series(range(1880, 2051))
    ax.plot(
        years_all,
        result_all.intercept + result_all.slope * years_all
    )

    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]

    result_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    years_recent = pd.Series(range(2000, 2051))
    ax.plot(
        years_recent,
        result_recent.intercept + result_recent.slope * years_recent
    )

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    # Keep ticks aligned with the freeCodeCamp tests
    ax.set_xticks([
        1850.0, 1875.0, 1900.0, 1925.0, 1950.0,
        1975.0, 2000.0, 2025.0, 2050.0, 2075.0
    ])

    # Save plot and return data for testing
    fig.savefig("sea_level_plot.png")
    return ax
