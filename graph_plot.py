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
def GraphPlotting(title, myXLabel=xLabel, myYLabel=yLabel):
    plt.xlabel(myXLabel)
    plt.ylabel(myYLabel)
    plt.title(title)
    plt.legend()
    plt.show()

# define a function 
def plot_graphs(url):
    """

    Parameters
    ----------
    url : str
        url containing the rainfall data of UK.

    Returns
    -------
    fetches the data from the url and plot graphs on it.

    """
    
    # fetch the data from url and read it into a DataFrame and print it
    rainfall_data = pd.read_csv(url, skiprows=5, delim_whitespace=True)
    print(rainfall_data)
    
    
    # MULTIPLE-LINE PLOT
    # from years 2019 to 2023 comparing the rainfall monthly
    selective_years = list(range(2019, 2024))
    
    # filtering the data for these years by boolean indexing isin()
    filtered_years_data = rainfall_data[rainfall_data['year'].isin(selective_years)]
    
    # plotting multiple line graph for selective years and comparing the rainfall monthly 
    plt.figure(figsize = (10, 6))
    
    for Years in selective_years :
        selective_years_data = filtered_years_data[filtered_years_data['year'] == Years]
        plt.plot(selective_years_data.columns[1:13], selective_years_data.values[0][1:13], label = f'year{Years}')
   
    """
    # setting lables and title and show legend
    plt.xlabel('Months')
    plt.ylabel('Rainfall (mm)')
    plt.title('Monthly Rainfall in UK for year 2019-2023')
    plt.legend()

    # show the plot
    plt.show()

    """
    
    # calling the function and passing arguments
    GraphPlotting(linePlotTitle)
   
    
    
    # BOX PLOT
    # Plotting a Box plot for monthly rainfall distribution for different years 
    plt.figure(figsize = (10, 6))
   
    # making a box plot for each month by dropping all other columns 
    rainfall_data.drop(['year', 'win', 'spr', 'sum', 'aut', 'ann'], axis=1).boxplot()
    
    # setting lables and title and show legend
    """
    plt.xlabel('Months')
    plt.ylabel('Rainfall (mm)')
    plt.title('A Box Plot Showing Monthly Rainfall Distribution in the UK')
    plt.xticks(rotation = 45)
    plt.grid(True)
   
    # show the plot
    plt.show()
    """
    # calling the function and passing arguments
    GraphPlotting(boxPlotTitle)

   
    
    # HISTOGRAM
    # For annual rainfall distribution plotting Histogram 
    plt.figure(figsize = (10, 6))
    
    #making a histogram for annual rainfall 
    plt.hist(rainfall_data['ann'], bins=20, color='lightblue', edgecolor='black')
    
    # setting lables and title and show legend
    """
    plt.xlabel('Annual Rainfall (mm)')
    plt.ylabel('Frequency')
    plt.title('A Histogram Showing Distribution of Annual Rainfall in the UK')
    
    # show the plot
    plt.show()
    """
    GraphPlotting(histoPlotTitle, 'Annual Rainfall (mm)', 'Frequency')

    
#url of the data
url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Rainfall/date/UK.txt"

#calling the function and passing the argument
plot_graphs(url)
