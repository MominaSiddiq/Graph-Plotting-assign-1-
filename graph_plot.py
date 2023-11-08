#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 18:14:36 2023

@author: macbook
"""

# import libraries
import pandas as pd
import matplotlib.pyplot as plt

# variables declaration and assignment
xLabel = "Month"
yLabel = "Rainfall (mm)"
linePlotTitle = 'Monthly Rainfall in UK for year 2019-2023'
boxPlotTitle = 'A Box Plot Showing Monthly Rainfall Distribution in the UK'
histoPlotTitle = 'A Histogram Showing Distribution of Annual Rainfall in the UK'


# defining a function for setting labels and show legends
def GraphLabeling(title, myXLabel = xLabel, myYLabel = yLabel):
    """

    Parameters
    ----------
    title : str
        title containing the title of graph.
    myXLabel : str
         contains the xlabel of graph and assigned a by default value to it.
    myYLabel : str
        contains the ylabel of graph and assigned a by default value to it. 

    Returns
    -------
    Nothing returns
    this function sets labels and show legends and graph.

    """

    plt.xlabel(myXLabel)
    plt.ylabel(myYLabel)
    plt.title(title)
    plt.legend()
    plt.show()


# defining a function to plot graphs on the given data set
def plot_graphs(url):
    """

    Parameters
    ----------
    url : str
        url containing the rainfall data of UK.

    Returns
    -------
    Nothing returns
    this function fetches the data from the url and plot graphs on it.

    """

    # fetch the data from url and read it into a DataFrame and print it
    rainfall_data = pd.read_csv(url, skiprows = 5, delim_whitespace = True)
    print(rainfall_data)

    # <-------------------------------------------------------------->
    # <--------------------- MULTIPLE-LINE PLOT---------------------->
    # <-------------------------------------------------------------->

    # from years 2019 to 2023 comparing the rainfall monthly
    selective_years = list(range(2019, 2024))

    # filtering the data for these years by boolean indexing isin()
    filtered_years_data = rainfall_data[rainfall_data['year'].isin(
        selective_years)]

    # plotting multiple line graph for selective years and comparing the rainfall monthly
    plt.figure(figsize = (10, 6))
    for Years in selective_years:
        selective_years_data = filtered_years_data[filtered_years_data['year'] == Years]
        plt.plot(selective_years_data.columns[1:13],
                 selective_years_data.values[0][1:13], label = f'year{Years}')

    # calling the function and passing arguments
    GraphLabeling(linePlotTitle)

    # <-------------------------------------------------------------->
    # <----------------------- BOX PLOT ----------------------------->
    # <-------------------------------------------------------------->

    # Plotting a Box plot for monthly rainfall distribution for different years
    plt.figure(figsize=(10, 6))

    # making a box plot for each month by dropping all other columns
    rainfall_data.drop(['year', 'win', 'spr', 'sum',
                       'aut', 'ann'], axis = 1).boxplot()

    # calling the function and passing arguments
    GraphLabeling(boxPlotTitle)

    # <-------------------------------------------------------------->
    # <-------------------- HISTOGRAM PLOT -------------------------->
    # <-------------------------------------------------------------->

    # For annual rainfall distribution plotting Histogram
    plt.figure(figsize = (10, 6))

    # making a histogram for annual rainfall
    plt.hist(rainfall_data['ann'], bins = 20,
             color = 'lightblue', edgecolor = 'black')

    # calling the function and passing arguments
    GraphLabeling(histoPlotTitle, 'Annual Rainfall (mm)', 'Frequency')


# Url of data
url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Rainfall/date/UK.txt"

# calling the function and passing the argument
plot_graphs(url)
