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

# Read file
df = pd.read_csv(file_name, sep = '\t', header=None)







