# Subject title: DSP301x_1.2-A_VN 
# Assignment: 02
# Name of project: Test Grade Calculator

import pandas as pd
import numpy as np

# Task 1
# 1.2. Write program that allow user to input filename
def getInput():
    filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
    return filename + ".txt"

# User input file name
file_name = getInput()

# 1.3 Print notice and 1.4 Use try/except
try: # 1.4 Use try/except
            # 1.2. Read file
            df = pd.read_csv(file_name, sep = '\t', header=None)

            # 1.3 In case of open file OK
            print("Successfully opened " + file_name)

except: # 1.4 Use try/except
            # 1.3 In case of file cannot open
            print("File cannot be found.")








