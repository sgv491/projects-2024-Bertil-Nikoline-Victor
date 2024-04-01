import seaborn as sns
import matplotlib.pyplot as plt

# Plot constants
PLOT_HEIGHT = 3
PLOT_WIDTH = 6


def line_plot_without_labels(data, title, xlabel, ylabel):
    
    # Creating a seaborn plot
    plt.figure(figsize=(PLOT_WIDTH, PLOT_HEIGHT))
    sns.lineplot(data=data, linewidth=2, marker='o', markersize=5)

    # Adding title and labels
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)

    # Adding grid and annotations
    plt.grid(True, linestyle='--', alpha=0.7)

    # Adding a custom color palette
    custom_palette = sns.color_palette("husl", 5)
    sns.set_palette(custom_palette)

    return plt

def line_plot_with_labels(data, title, xlabel, ylabel, xName, yName):
    
    # Creating a seaborn plot
    plt.figure(figsize=(PLOT_WIDTH, PLOT_HEIGHT))
    sns.lineplot(data=data, x=xName, y=yName, linewidth=2, marker='o', markersize=5)

    # Adding title and labels
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)

    # Adding grid and annotations
    plt.grid(True, linestyle='--', alpha=0.7)

    # Adding a custom color palette
    custom_palette = sns.color_palette("husl", 5)
    sns.set_palette(custom_palette)

    return plt