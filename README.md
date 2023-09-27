# CollatzProblem
 
My approach to anlyzing Collatz Problem, using Python. 


File **collatz_data_20kk_v2-gz.parquet** - dataset used for this analyze.

File **collatz_problem_v1.py** - is used to generate dataset, you can change number of generated rows by variable **last_number**.

File **collatz_analyze.py** contains 4 functions:
 - load_parquet_data - loads dataset from .parquet file
 - intro_analyze - returns head, tail and pd.describe of loaded dataset.
 - draw_plot - draws two plots in one window: on axel X - consecutive natural numbers, on axel Y1 - number of steps needed to resolve Collatz Problem for given natural, Y1 Steps_y divided by Number_x number.
 - draw_histogram - draws histograph: on axel X - count of steps, on axel Y - how many times given count of steps occurs/repeats in dataset.
