import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

def load_parquet_data(path):
    df = pd.read_parquet(path)
    return df


def intro_analyze(path):
    df = load_parquet_data(path)
    pd.set_option('display.float_format', lambda x: '%.4f' % x)
    df = df.assign(Steps_by_number=df['Steps_y'] / df['Number_x'])
    df2 = df.query('Steps_y == 0 or `Number_x` == 0')
    # print(df2)
    # df2 = df.drop([0, 1])
    # df2 = df2.assign(steps_by_number=df['Number (x)'] / ['Steps (y)'])
    # print('df2: ', df2.head())
    print(df.info())
    df_head = df.head(30)
    # df_head_ass = df_head.assign(steps_by_number=df_head['Steps (y)']/df_head['Number (x)'])
    df_tail = df.tail()
    df_describe = df.describe()
    # df_min = df.min()
    # df_max = df.max()

    df_count_155 = df[df.Steps_y == 120].count()
    df_count = df.Steps_y.value_counts()
    # df_count_155 = df[df.steps_by_number == 0.5].count()
    # df_count_155 = df[df.Steps_y == 155].count()


    print(
          f'\033[1m*|* Summary of analyze: \033[0m\n\n '
          f'** Head is: \n{df_head} **\n '
          f'** 155 steps occurs: \n{df_count_155} **\n '
          f'** Count of steps is: \n{df_count} **\n '
          # f'** Head with Steps / Nmber: \n{df_head_ass} **\n '
          f'** Tail is: \n{df_tail} **\n '
          # f'** Describe is: \n{df_describe} **\n '
          # f'** Minimal Value is: \n{df_min} **\n '
          # f'** Maximal Value is: \n{df_max} **\n\n'
    )

    return df


def draw_plot(path):
    # load data for plots
    plot_df = load_parquet_data(path)
    plot_df_ratio = intro_analyze(path)
    # assign specific series of Data Frame to variables
    x = plot_df.loc[:, 'Number_x'] # is it possible it's more optimasie than df['Number_x'] in  ax2.scatter
    y = plot_df.loc[:, 'Steps_y']
    ratio = plot_df_ratio.loc[:, 'Steps_by_number']
    # draw y(x) plot
    fig, ax1 = plt.subplots()
    color_ax1 = 'green'
    ax1.set_xlabel('Number *N*', color='black')
    ax1.set_ylabel('Count of Steps', color=color_ax1)
    ax1.scatter(x, y, s=0.001, c=color_ax1)
    ax1.tick_params(axis='y', labelcolor=color_ax1)
    # instantiate a second axes that shares the same x-axis
    ax2 = ax1.twinx()
    # draw ratio(x) plot
    ax2.set_ylabel('Steps to Number Ratio', color="red")
    color_ax2 = 'red'
    ax2.scatter(x, ratio, s=0.1, c=color_ax2)
    ax2.tick_params(axis='y', labelcolor=color_ax2)

    plt.grid(True)
    fig.tight_layout()


def draw_histogram(path):
    hist_df = load_parquet_data(path)
    n_steps = hist_df.loc[:, 'Steps_y']
    fig, axs = plt.subplots(tight_layout=True)
    axs.hist(n_steps, bins=700)
    axs.set_xlabel('Count of Steps', color='blue')
    axs.set_ylabel('How many times occurs', color='black')

    plt.show()


if __name__ == '__main__':
    DATA_PATH = "collatz_data_20kk_v2-gz.parquet"
    print(f' ** End of Collatz Problem analyze: {intro_analyze(DATA_PATH)} ** \n')
    print(f' ** Draw plot: {draw_plot(DATA_PATH)}')
    print(f' ** Draw histogram: {draw_histogram(DATA_PATH)}')
