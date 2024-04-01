import seaborn as sns
import matplotlib.pyplot as plt

def pretty_line_plot_US(data, title, xlabel, ylabel):
    
    # Creating a seaborn plot
    plt.figure(figsize=(8, 4))
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

def pretty_line_plot_DK(data, title, xlabel, ylabel, xName, yName):
    
    # Creating a seaborn plot
    plt.figure(figsize=(8, 4))
    sns.lineplot(data=data, x=xName, y=yName, color='skyblue', linewidth=2, marker='o', markersize=5)

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