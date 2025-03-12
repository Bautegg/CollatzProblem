import concurrent.futures
import multiprocessing
import os
import matplotlib.pyplot as plt
import pandas as pd
from collatz_analyze import draw_plot, draw_histogram


def collatz_steps(n):
    """Calculate the number of steps to reach 1 in the Collatz sequence for a given n number."""
    steps = 0
    if (n % log_cycle) == 0:
        print(n)
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def compute_collatz_parallel(last_number, num_workers):
    """
    Compute Collatz steps using multiprocessing and store results in a Pandas DataFrame.
    :param last_number: Number of natural numbers to compute.
    :param num_workers: Number of processes to use (default: CPU count).
    """
    
    numbers = list(range(1, last_number + 1))

    # Use multiprocessing Pool for parallel execution
    with multiprocessing.Pool(processes=num_workers) as pool:
        steps = pool.map(collatz_steps, numbers)  # Map function across processes

    df = pd.DataFrame({"Steps": steps}, index=range(1, last_number + 1))
    return df

if __name__ == "__main__":
    num_workers = None # put number of cores or None to use all available cores
    last_number = 500000 # last number included into result file
    log_cycle = 100000 # how often script progress is printed

    if f'{num_workers}'.isdecimal():
        print(f"Using {num_workers} CPU cores for computation...")   
    elif num_workers is None:
        num_workers = multiprocessing.cpu_count()  # Use all available CPU cores
        print(f"Using all {num_workers} CPU cores for computation...") 
    
    df = compute_collatz_parallel(last_number, num_workers)
    print(df)

    
    folder_name = 'artifacts'
    file_name = f'collatz_data_{last_number/1000000}kk_brotli.parquet'
    
    
    os.makedirs(folder_name, exist_ok=True)
    file_path = os.path.join(folder_name, file_name)

    # save df to parquet file
    df.to_parquet(file_path, index=True, engine='pyarrow', compression='brotli')

    # execution of collatz_analyze.py    
    draw_plot(file_path) 
    draw_histogram(file_path)
    plt.show()
