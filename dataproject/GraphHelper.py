import seaborn as sns
import matplotlib.pyplot as plt



############################
#     Time series plot     #
############################


def line_plot_with_labels(data, title, xlabel, ylabel, xName, yName, color="orange"):
    
    # Creating a seaborn plot
    plt.figure(figsize=(6, 4))
    sns.lineplot(data=data, x=xName, y=yName, linewidth=1.5, color=color, marker='o', markersize=5)

    # Adding title and labels
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=11)
    plt.ylabel(ylabel, fontsize=11)

    # Adding grid and annotations
    plt.grid(True, linestyle='--', alpha=0.7)

    # Adding a custom color palette
    custom_palette = sns.color_palette("husl", 5)
    sns.set_palette(custom_palette)

    return plt



##########################
#     Phillips Curve     #
##########################

def plot_philips_curve_static(data, xName, yName, title):

    # Create scatter plot with tendency line
    plt.figure(figsize=(5, 5))  # Set figure size

    # Set Seaborn style and context
    sns.set_style("whitegrid")
    sns.set_context("notebook", font_scale=1.2)

    # Scatter plot
    sns.scatterplot(data=data, x=xName, y=yName, color='gray', alpha=0.7, label='Data')

    # Tendency line - Exponential
    (xValues, yValues) = calculate_exponential_fit(data[xName], data[yName])

    # Plot exponential curve
    plt.plot(xValues, yValues, color='red', linewidth=2, linestyle='dashed', label='Exponential Regression')


    # Adjust tick font size
    plt.xticks(fontsize=10)  # Increase tick label font size
    plt.yticks(fontsize=10)  # Increase tick label font size


    plt.grid(True, linestyle='--', alpha=0.7)  # Add gridlines with dashed style and reduced opacity
    plt.legend(loc='upper right', fontsize=10)  # Add a legend with increased font size
    plt.tight_layout()  # Adjust plot layout for better presentation


    # Set limits on the x and y axes
    #plt.xlim(2, 7)  # Set x-axis limits
    plt.ylim(2, 7)  # Set y-axis limits

    # Add title and labels
    plt.title(title, fontsize=14)
    plt.xlabel('Unemployment rate (pct.)', fontsize=11)
    plt.ylabel('Inflation rate (pct.)', fontsize=11)

    # Add legend
    plt.legend()

    # Change legend font size
    plt.legend(fontsize=12)

    return plt




###########################
#     Exponential fit     #
###########################

from scipy.optimize import curve_fit
import numpy as np

def calculate_exponential_fit(x, y):

    # Define an exponential function
    def exponential_func(x, a, b):
        return a * np.exp(b * x)

    # Fit the exponential curve to the data
    popt, pcov = curve_fit(exponential_func, x, y)

    # Modify parameters for steeper slope
    popt[1] *= 1.0  # Adjust the slope parameter b to increase the slope

    # Generate points for the exponential curve
    x_values = np.linspace(min(x) - 1, max(x) + 1, 100)
    y_values = exponential_func(x_values, *popt)

    return (x_values, y_values)