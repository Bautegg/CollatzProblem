import pandas as pd
import concurrent.futures
import multiprocessing

def collatz_steps(n):
    """Calculate the number of steps to reach 1 in the Collatz sequence for a given n number."""
    steps = 0
    if (n % LOG_CYCLE) == 0:
        print(n)
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def compute_collatz_parallel(last_number, num_workers=None):
    """
    Compute Collatz steps using multiprocessing and store results in a Pandas DataFrame.
    :param last_number: Number of natural numbers to compute.
    :param num_workers: Number of processes to use (default: CPU count).
    """
    if num_workers is None:
        num_workers = multiprocessing.cpu_count()  # Use all available CPU cores
    
    numbers = list(range(1, last_number + 1))

    # Use multiprocessing Pool for parallel execution
    with multiprocessing.Pool(processes=num_workers) as pool:
        steps = pool.map(collatz_steps, numbers)  # Map function across processes

    # Store results in a DataFrame
    df = pd.DataFrame({"Steps": steps}, index=range(1, last_number + 1))
    return df

if __name__ == "__main__":
    last_number = 5000000
    LOG_CYCLE = 10000000

    num_workers = multiprocessing.cpu_count()  # Use all available CPU cores

    print(f"Using {num_workers} CPU cores for computation...")
    
    df = compute_collatz_parallel(last_number, num_workers)
    
    print(df)  # Display DataFrame
    df.to_parquet(f'collatz_data_{last_number/1000000}kk_v4_brotli.parquet', index=True, engine='pyarrow', compression='brotli')
