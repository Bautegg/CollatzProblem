import pandas as pd


def collatz_for(last_number):
    """

    :param last_number: int - the last number which will be displayed at the end of X axis on the plot
    :return: dict - Key of plot_dictionary is argument of X axis on the plot, Value of plot_dictionary
    is value of Y axis on the plot
    """
    LOG_CYCLE = last_number / 10
    plot_dictionary = {}
    for number in range(last_number+1):
        if (number % LOG_CYCLE) == 0:
            print(number)
        first_number = number
        steps = 0
        while number > 1:
            steps += 1
            if number % 2 == 0:
                number = number / 2
            else:
                number = 3 * number + 1
                plot_dictionary[first_number] = steps
    return plot_dictionary


def create_frame(last_number):

    frame_data = collatz_for(last_number)
    frame_data1 = {'Number_x': frame_data.keys(), 'Steps_y': frame_data.values()}
    df1 = pd.DataFrame.from_dict(frame_data1)
    print(df1)
    df1.to_parquet('collatz_test_v1_10k-gz.parquet', index=False, compression='gzip')

if __name__ == '__main__':
    last_number = 10000000

    print(f'Create_DataFrame and .csv: {create_frame(last_number)}')

