import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv("epa-sea-level.csv")
    x = data['Year']
    y = data['CSIRO Adjusted Sea Level']
    # Create scatter plot
  
    figure,ax= plt.subplots(figsize=(12,5))
    plt.scatter(x,y)

    # Create first line of best fit
    res = linregress(x,y)
    xpred = pd.Series([i for i in range(1880,2051)])
    ypred = res.slope*xpred + res.intercept
    plt.plot(xpred,ypred,'r')

    # Create second line of best fit
    new_data = data.loc[data['Year']>=2000]
    new_x = new_data['Year']
    new_y = new_data['CSIRO Adjusted Sea Level']
    res1 = linregress(new_x,new_y)
    xpred1 = pd.Series([i for i in range(2000,2051)])
    ypred1 = res1.slope*xpred1 + res1.intercept
    plt.plot(xpred1,ypred1,'green')
    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel( "Year")
    ax.set_ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()