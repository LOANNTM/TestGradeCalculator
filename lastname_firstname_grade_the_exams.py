# Subject title: DSP301x_1.2-A_VN 
# Assignment: 02
# Name of project: Test Grade Calculator

import os
import sys
import pandas as pd
import numpy as np

answer_key = ['B', 'A', 'D', 'D', 'C', 'B', 'D', 'A', 'C', 'C', 'D', 'B', 'A', 'B', 'A', 'C', 'B', 'D', 'A', 'C', 'A', 'A', 'B', 'D', 'D'] # Use for Task3 this is answer key data
result_list = np.array([], dtype='i4') # Use for Task3 to store the score of student

question_skip = np.empty(25, dtype='i4') # Use for 3.7
question_skip.fill(0) # Fill default data by zero [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

question_incorrectly = np.empty(25, dtype='i4') # Use for 3.8
question_incorrectly.fill(0) # Fill default data by zero [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Task 1
# 1.2. Write program that allow user to input filename
def getInput():
    filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
    return filename + ".txt"

# Task 2
def data_analyze(df, file_result):
    global result_list
    result_list = np.array([], dtype='i4') #use for 3.1
    
    print("** ANALYZING **")
    total_valid_lines = 0
    total_invalid_lines = 0
    for index, row in df.iterrows():
        line_data = row[0] # N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D
        sep_line_data = line_data.split(",") # ['N12345678', 'B', 'A', 'D', 'D', 'C', 'B', 'D', 'A', 'C', 'C', 'D', 'B', 'A', 'B', 'A', 'C', 'B', 'D', 'A', 'C', 'A', 'A', 'B', 'D', 'D']
        
        # Check if data enough 26 data
        if len(sep_line_data) == 26:
            # Check ID is valid or not. Valid: N00000021, invalid: N0000002, invalid: NA0000027
            ID = sep_line_data[0]
            if ID[0] != "N" or len(ID) != 9: # Check ID start by 'N' and length is 9
                total_invalid_lines = total_invalid_lines + 1
                print("Invalid line of data: N# is invalid")
                print(line_data)
            else:
                ID_number = ID[1:] # Convert from NA0000027 -> A0000027
                if ID_number.isdigit(): # In case of number only 00000021
                    total_valid_lines = total_valid_lines + 1
                     # Only getScore for valid data - Task 3.1
                    answer_list = sep_line_data[1:] # Remove ID: ['B', 'A', 'D', 'D', 'C', 'B', 'D', 'A', 'C', 'C', 'D', 'B', 'A', 'B', 'A', 'C', 'B', 'D', 'A', 'C', 'A', 'A', 'B', 'D', 'D']
                    score = getScore(answer_list)
                    result_list = np.append(result_list, score)

                     # Task 4:
                    print(str(ID) + "," + str(score), file=file_result)
                else: # In case of none number only A0000027
                    total_invalid_lines = total_invalid_lines + 1
                    print("Invalid line of data: N# is invalid")
                    print(line_data)
        else:
            print("Invalid line of data: does not contain exactly 26 values:")
            print(line_data)
            total_invalid_lines = total_invalid_lines + 1
            
    if total_invalid_lines == 0:
        print("No errors found!")
    print("** REPORT **")
    print("Total valid lines of data: " + str(total_valid_lines))
    print("Total invalid lines of data: " + str(total_invalid_lines))

    # Task 3
    # Input is the array with ID and answer_list: ['B', 'A', 'D', 'D', 'C', 'B', 'D', 'A', 'C', 'C', 'D', 'B', 'A', 'B', 'A', 'C', 'B', 'D', 'A', 'C', 'A', 'A', 'B', 'D', 'D']
def getScore(answer_list):
    global question_skip

    score = 0
    for index in range(0, len(answer_list)):
        if answer_list[index] == answer_key[index]: # +4 for correct answer
            score = score + 4
        elif answer_list[index] == "": # 0 in case of empty answer
            score = score + 0

            # Calculate 3.7
            question_skip[index] = question_skip[index] + 1
        else: # -1 in case of wrong answer
            score = score - 1

             # Calculate 3.8
            question_incorrectly[index] = question_incorrectly[index] + 1

    return score

# 3.1 - 3.2 - 3.3 - 3.4 - 3.5 - 3.6 - 3.7 - 3.8
def statistic_for_class():
    global result_list

    # 3.1. Count number of student with high score (>80).
    total_student_of_high_scores = np.count_nonzero(result_list > 80)
    print("Total student of high scores: " + str(total_student_of_high_scores))

    # 3.2. Mean.
    mean = np.mean(result_list)
    print("Mean (average) score: " + str(mean))

    # 3.3. Hightest score.
    highest_score = np.max(result_list)
    print("Highest score: " + str(highest_score))

    # 3.4. Lowest score.
    lowest_score = np.min(result_list)
    print("Lowest score: " + str(lowest_score))

    # 3.5. Range of scores.
    range_of_scores = highest_score - lowest_score
    print("Range of scores: " + str(range_of_scores))

    # 3.6. Median score
    median_score = np.median(result_list)
    print("Median score: " + str(median_score))

    # 3.7. Question that most people skip
    # After calculate we have the list of Question that most people skip like [3 2 4 3 4 1 3 0 1 1 3 2 1 1 1 1 2 0 2 3 3 3 4 3 1]
    
    most_people_skip= np.max(question_skip)
    question_that_most_people_skip = ""
    for index in range(0, len(question_skip)):
        if question_skip[index] == most_people_skip:
            if question_that_most_people_skip == "":
                question_that_most_people_skip = str(index + 1) + " - " + str(most_people_skip) + " - " + str(most_people_skip / len(result_list))
            else:
                question_that_most_people_skip = question_that_most_people_skip + ", " + str(index + 1) + " - " + str(most_people_skip) + " - " + str(most_people_skip / len(result_list))
    print("Question that most people skip: " + question_that_most_people_skip)

# 3.8. Question that most people answer incorrectly
    most_people_answer_incorrectly = np.max(question_incorrectly)
    question_that_most_people_answer_incorrectly = ""
    for index in range(0, len(question_incorrectly)):
        if question_incorrectly[index] == most_people_answer_incorrectly:
            if question_that_most_people_answer_incorrectly == "":
                question_that_most_people_answer_incorrectly = str(index + 1) + " - " + str(most_people_answer_incorrectly) + " - " + str(most_people_answer_incorrectly / len(result_list))
            else:
                question_that_most_people_answer_incorrectly = question_that_most_people_answer_incorrectly + ", " + str(index + 1) + " - " + str(most_people_answer_incorrectly) + " - " + str(most_people_answer_incorrectly / len(result_list))
    print("Question that most people answer incorrectly: " + question_that_most_people_answer_incorrectly) 

# Task 4 creat file result

# Main function
def main():
    global question_skip # use for 3.7
    global question_incorrectly # use for 3.8

    while 1:
        is_file_open = False
        # User input file name
        file_name = getInput()
        df = None
        file_result = None
        try: # 1.4 Use try/except
            # 1.2. Read file
            df = pd.read_csv(file_name, sep = '\t', header=None)

            # 1.3 In case of open file OK
            print("Successfully opened " + file_name)

            # Task 4:
            file_result = open(file_name.replace(".", "_grades."), "w")

            is_file_open = True
        except: # 1.4 Use try/except
            # 1.3 In case of file cannot open
            print("File cannot be found.")

        # If file is opened OK
        if is_file_open == True:
            question_skip = np.empty(25, dtype='i4') # Use for 3.7
            question_skip.fill(0) # Fill default data by zero [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] use for 3.7

            question_incorrectly = np.empty(25, dtype='i4') # Use for 3.8
            question_incorrectly.fill(0) # Fill default data by zero [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] use for 3.8
    
            data_analyze(df, file_result)

             # Task 3:
            statistic_for_class()

             # Task 4:
            file_result.close()

# Call Main function
if main() == False:
    sys.exit(-1)






