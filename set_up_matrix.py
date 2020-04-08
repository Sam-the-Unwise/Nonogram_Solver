###############################################################################
#
# Author: Samantha Muellner
# Version: 1.0
# Description: A simple code that solves nonograms. The input to the code comes
#   in the form of:
#       num_of_rows
#       num_of_cols
#       columns
#       rows
#
###############################################################################
'''
AUTHOR: Samantha Muellner

DESCRIPTION: File that will take in input and set up nonogram as needed

VERSION: 1.1.0v
'''

from solve_nonogram import calculate_nonogram
from print_nonogram import print_matrix

def correctly_store_column_input(col_amount):
    # create list that will hold final output
    column_input_correct = False

    while column_input_correct is False:
        columns = []

        # assume that the correct input will be given
        column_input_correct = True

        #columns_format = input("Enter column format: ")
        columns_format = '"5", "2,2", "1,1", "2,2", "5"'

        column_list = columns_format.split("\", \"")

        # before this loop in format of '"5' or '3,3' or '4,4,4"'
        # these must be changed to be [5], [3, 3], [4, 4, 4]
        for sub_list in column_list:
            # create list that will hold the different aspects of our column
            sub_column_components_list = []
            sub_column_components = sub_list.split(',')

            # sum variable that will determine if the numbers entered are compatable
            col_sum = 0

            # loop through the different numbers in our sub_col_com_list
            # before this loop in format of ['"5', '3', '3'] or ['4', '4', '4"']
            for number in sub_column_components:
                number = int(number.replace('"', ''))
                col_sum += number

                # if 6 has been entered but they're are only 5 columns, throw error
                if number > col_amount:
                    print("One number inputted for column is larger than column size")
                    print("Please input smaller number than " + str(col_amount))
                    print("\n")
                    
                    column_input_correct = False

                sub_column_components_list.append(number)
            
            if col_sum > col_amount:
                print("Numbers inputed for one of columns has too great a sum")
                print("Please enter a new amount that contains numbers less than the columns length of " + str(col_amount))
                print("\n")
                
                column_input_correct = False

            columns.append(sub_column_components_list)

    
    return columns


def correctly_store_row_input(row_amount):

    row_input_correct = False

    while row_input_correct is False:
        # create list that will hold final output
        rows = []

        # assume that the correct input will be given
        row_input_correct = True

        # row_format = input("Enter row format: ")
        row_format = '"5", "2,2", "1,1", "2,2", "5"'

        row_list = row_format.split("\", \"")

        # now in format of '"5' or '3,3' or '4,4,4"'
        # these must be changed to be [5], [3, 3], [4, 4, 4]
        for sub_list in row_list:
            # create list that will hold the different aspects of our row
            sub_row_components_list = []
            sub_row_components = sub_list.split(',')

            row_sum = 0

            # loop through the different numbers in our sub_col_com_list
            # now in format of
            for number in sub_row_components:
                number = int(number.replace('"', ''))

                # if 6 has been entered but they're are only 5 columns, throw error
                if number > row_amount:
                    print("One number inputted for row is larger than row size")
                    print("Please input smaller number than " + str(row_amount))
                    print("\n")

                    row_input_correct = False

                sub_row_components_list.append(number)

            if row_sum > row_amount:
                print("Numbers inputed for one of rows has too great a sum")
                print("Please enter a new amount that contains numbers less than the rows length of " + str(row_amount))
                print("\n")
                
                row_input_correct = False

            rows.append(sub_row_components_list)
    
    return rows


# function that will equalize our list so a list of [[5], [4, 1]] will become 
#      [[0, 5], [4, 1]]
# NOTE: This is merely for printing purposes
def equalize_list(list_of_numbers):
    # get max amount of items
    max_item_amount = 0

    list_of_nums = []

    # create duplicate list so we don't change the original
    # NOTE: for some reason directly doing list_of_nums = list_of_numbers.copy() did not work
    for n_list in list_of_numbers:
        list_of_nums.append(n_list.copy())

    
    # loop through to get the largest item
    for item in list_of_nums:
        if len(item) > max_item_amount:
            max_item_amount = len(item)

    # loop through again an edit each vector
    #   set 0s in front of vector so that it is the same size as the max
    for num_list in list_of_nums:
        while len(num_list) is not max_item_amount:
            num_list.insert(0, 0)

    return list_of_nums

# function that will simply create a blank matrix
def create_matrix(num_rows, num_cols):
    output_matrix = []

    for number in range(num_rows):
        row_matrix = []

        for count in range(num_cols):
            row_matrix.append(0)
        
        output_matrix.append(row_matrix)
    
    return output_matrix




# get the input from the user for the design of the matrix
def get_input():
    # create boolean variables that will check if the numbers inputed for the column
    #       and row are within reason -- use for a loop that will reask for the column
    #       or row inputs 
    #           Ex: if the number of columns is 5 and an input is 6, this is not correct
    row_input_correct = False

    # num_rows = int(input("Number of rows: "))
    # num_cols = int(input("Number of cols: "))
    #print("\n")

    num_rows = 5
    num_cols = 5

    # print("Please enter row and column numbers in the following format if wishing to have 5 in the first row, then 3 and 3 in the second, then 1 and 2 and 1 in the third")
    # print('Example Row format: "5", "3,3", "1,2,1"\n')

    column_list = correctly_store_column_input(num_cols)
    row_list = correctly_store_row_input(num_rows)

    # get column and row amounts that are equalized (aka, [[5], [2,2]] is now [[0,5], [2,2]])
    #   NOTE: these should only be used for printing
    equalized_column_list = equalize_list(column_list)
    equalized_row_list = equalize_list(row_list)

    blank_matrix = create_matrix(num_rows, num_cols)

    print("Here is the current set up of your matrix--matrix itself is currently blank")
    print_matrix(blank_matrix, equalized_row_list, num_rows, equalized_column_list, num_cols)

    calculate_nonogram(blank_matrix, equalized_row_list, num_rows, equalized_column_list, num_cols)