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

# Url of data
url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Rainfall/date/UK.txt"

xLabel = "Month"
yLabel = "Rainfall (mm)"

linePlotTitle = 'Monthly Rainfall in UK for year 2019-2023 (Multiple-line Plot)'
boxPlotTitle = 'Monthly Rainfall Distribution in the UK (Box Plot)'
histoPlotTitle = 'Distribution of Annual Rainfall in the UK (Histogram)'

figX_Size = 10
figY_Size = 6



# defining a function for setting labels and show legends
def GraphLabelingAndShow(title, myXLabel = xLabel, myYLabel = yLabel):
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


def PlotFigure(xSize = figX_Size, ySize = figY_Size):
    plt.figure(figsize = (xSize, ySize))



# <-------------------------------------------------------------->
# <--------------------- MULTIPLE-LINE PLOT---------------------->
# <-------------------------------------------------------------->

def plot_line_graph(data):
    """

    Parameters
    ----------
    data : csv
        data containing the rainfall data of UK.

    Returns
    -------
    Nothing returns
    this function taking data and plot line graph on it.

    """

    # from years 2019 to 2023 comparing the rainfall monthly
    selective_years = list(range(2019, 2024))

    # filtering the data for these years by boolean indexing isin()
    filtered_years_data = data[data['year'].isin(
        selective_years)]

    # plotting multiple line graph for selective years and comparing the rainfall monthly
   
    # calling the function to plot figure
    PlotFigure()

    for Years in selective_years:
        selective_years_data = filtered_years_data[filtered_years_data['year'] == Years]
        plt.plot(selective_years_data.columns[1:13],
                 selective_years_data.values[0][1:13], label = f'year{Years}')

    # calling the function for labelling and showing graph
    GraphLabelingAndShow(linePlotTitle)



# <-------------------------------------------------------------->
# <----------------------- BOX PLOT ----------------------------->
# <-------------------------------------------------------------->

def box_plot(data):
    """

    Parameters
    ----------
    data : csv
        data containing the rainfall data of UK.

    Returns
    -------
    Nothing returns
    this function taking data and plot box plot on it.

    """

    # Plotting a Box plot for monthly rainfall distribution for different years
    
    # calling the function to plot figure
    PlotFigure()

    # making a box plot for each month by dropping all other columns
    data.drop(['year', 'win', 'spr', 'sum',
                       'aut', 'ann'], axis = 1).boxplot()

    # calling the function for labelling and showing graph
    GraphLabelingAndShow(boxPlotTitle)



# <-------------------------------------------------------------->
# <-------------------- HISTOGRAM PLOT -------------------------->
# <-------------------------------------------------------------->

def plot_histogram(data):
    """

    Parameters
    ----------
    data : csv
        data containing the rainfall data of UK.

    Returns
    -------
    Nothing returns
    this function taking data and plot histogram on it.

    """

    # For annual rainfall distribution plotting Histogram
    
    # calling the function to plot figure
    PlotFigure()

    # making a histogram for annual rainfall
    plt.hist(data['ann'], bins = 20,
             color = 'lightblue', edgecolor = 'black')

    # calling the function for labelling and showing graph
    GraphLabelingAndShow(histoPlotTitle, 'Annual Rainfall (mm)', 'Frequency')



def FetchingDataFromURL():
    """

    Parameters
    ----------
    No parameters

    Returns
    -------
    Nothing returns
    this function fetch the data from url and read it 
    into a DataFrame and print it

    """
    
    global rainfall_data
    rainfall_data = pd.read_csv(url, skiprows = 5, delim_whitespace = True)
    print(rainfall_data)



def GraphPlot(data):
    """

    Parameters
    ----------
    data : csv
        data containing the rainfall data of UK.

    Returns
    -------
    Nothing returns
    this function calling three types of graph plotting functions 
    and passing data as an argument

    """
   
    # calling the functions and passing the argument
    plot_line_graph(data)
    box_plot(data)
    plot_histogram(data)



# calling the data fech and main graph plotting function
FetchingDataFromURL()
GraphPlot(rainfall_data)
