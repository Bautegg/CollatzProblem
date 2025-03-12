# CollatzProblem WIP
 
My approach to anlyzing Collatz Problem, using Python. 

How to run it?

Check **requirements.txt** if you have all needed libraries in your virtual enviroment. Then run **main.py**, you will see progressing numbers in terminal. When process finish you will find result .parquet file in **artifacts** folder and two charts will appear.

**last_number** - Define last number included into result file. Be carefull with increasing this number, as this script use all CPU cores and it could take time to generate (time will depend from your machine). Monitor your CPU temperature when script is running.
**log_cycle** - define how often script progress is printed


