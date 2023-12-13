import pandas as pd


def collatz_for(last_number):
    """
    :param last_number: int - the last number which will be displayed at the end of X axis on the plot
    :return: list - number of steps needed to finalize Collatz Problem for each number (index)
    """
    LOG_CYCLE = last_number / 10
    step_list = []
    for number in range(last_number + 1):
        if (number % LOG_CYCLE) == 0:
            print(number)
        steps = 0
        while number > 1:
            steps += 1
            if number % 2 == 0:
                number = number / 2
            else:
                number = 3 * number + 1
        step_list.append(steps)
    return step_list

def create_frame():
    df = pd.DataFrame(collatz_for(last_number), columns=['Number_of_steps'])
    print(df)
    df.to_parquet('collatz_test_v2_10k-gz.parquet', index=True, compression='gzip')


if __name__ == '__main__':
    last_number = 10000000

    # print(f'Number of steps: {collatz_for(last_number)}')
    print(f'df is: \n {create_frame()}')
