import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date', parse_dates=True)

# Clean data
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)

df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]

def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['value'], color='blue', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig = plt.gcf()
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    # Draw bar plot
    plt.figure(figsize=(10, 6))
    df_bar.plot(kind='bar', legend=True)
    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig = plt.gcf()
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')

    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=[
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    for ax in axes:
        ax.set_xlabel('Year' if ax == axes[0] else 'Month')
        ax.set_ylabel('Page Views')
        
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
