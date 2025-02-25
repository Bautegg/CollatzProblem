import pandas as pd
import matplotlib.pyplot as plt





def load_parquet_data(path):
    df = pd.read_parquet(path, engine='pyarrow')
    df['index_col'] = df.index

    return df


def intro_analyze(path):
    df = load_parquet_data(path)
    steps_y = df['Steps']
    number_x = df['index_col']
    
    pd.set_option('display.float_format', lambda x: '%.4f' % x)
    df = df.assign(Steps_by_number=steps_y / number_x)
    df2 = df.query(f'Steps == 0 or index_col == 0')
    print(df2)
    print(df.info())
    df_head = df.head(30)
    df_tail = df.tail()
    df_describe = df.describe()

    print(
          f'\033[1m*|* Summary of analyze: \033[0m\n\n '
          f'** Head is: \n{df_head} **\n '
          f'** Tail is: \n{df_tail} **\n '
          f'** Describe is: \n{df_describe} **\n '
    )

    return df


def draw_plot(path):
    # load data for plots
    plot_df = intro_analyze(path)
    # assign specific series of Data Frame to variables
    x = plot_df.loc[:, 'index_col']
    y = plot_df.loc[:, 'Steps']
    ratio = plot_df.loc[:, 'Steps_by_number']
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
    ax2.scatter(x, ratio, s=0.0001, c=color_ax2)
    ax2.tick_params(axis='y', labelcolor=color_ax2)

    plt.grid(True)
    fig.tight_layout()
  
  
def draw_histogram(path):
    hist_df = load_parquet_data(path)
    n_steps = hist_df.loc[:, 'Steps']
    fig, axs = plt.subplots(tight_layout=True)
    axs.hist(n_steps, bins=700)
    axs.set_xlabel('Count of Steps', color='blue')
    axs.set_ylabel('How many times occurs', color='black')




if __name__ == '__main__':
    DATA_PATH = "collatz_data_5.0kk_v4_brotli.parquet"
    draw_plot(DATA_PATH)
    draw_histogram(DATA_PATH)
    plt.show()
