'''
AUTHOR: Samantha Muellner

DESCRIPTION: File that will perform all computations needed in order to solve 
                the nonogram

VERSION: 1.0.2v
'''
from print_nonogram import print_matrix

def calculate_nonogram(matrix, row_list, num_rows, column_list, num_cols):
    # get the max amount of items
    # note that since this passes in the equalized cols and rows, we can just use the first
    #       element to calculate this
    max_row_item_amount = len(row_list[0])

    # create variables that will be modified when possibly filling all the rows or columns
    #       of a section of matrix
    num_rows_that_can_be_filled = num_rows
    num_columns_that_can_be_filled = num_cols

    # search through rows to see if any of them are the same length as the column
    for row in range(num_rows):
        for count in range(max_row_item_amount):

            # if any of our inputs in our row list are equal to the max number
            #   of columns, go through and modify all cells in that row
            if row_list[row][count] == num_columns_that_can_be_filled:
                matrix, row_list[row][count] = add_all_to_row(matrix, 
                                                              row, 
                                                              count,
                                                              row_list, 
                                                              column_list)
                # since we have now filled an entire row of the matrix, there
                #   is one less row that can be filled
                # this variable will be used in the next for loop
                num_rows_that_can_be_filled -= 1


    print("....solving.....\n")
    print_matrix(matrix, row_list, num_rows, column_list, num_cols)

    # search through columns to see if any of them are the same length as the rows
    for col in range(num_rows):
        for count in range(max_row_item_amount):
            if row_list[col][count] == num_rows_that_can_be_filled:
                matrix, column_list[col][count] = add_all_to_col(matrix, 
                                                                 col, 
                                                                 count, 
                                                                 column_list, 
                                                                 row_list)

    print("....solving.....\n")
    print_matrix(matrix, row_list, num_rows, column_list, num_cols)


# function that will handle if a row says to fill all it's columns
def add_all_to_row(matrix, row_to_modify, count_to_modify, row_list, column_list):
    # get the count supplied in the row list
    num_to_modify = row_list[row_to_modify][count_to_modify]


    # modified_matrix = list(matrix)

    # loop through row
    for col_section in matrix[row_to_modify]:
        matrix[row_to_modify][col_section] = "[]"

    # loop through and negate values from columns as needed
    for col_int in range(len(row_list)):
        modified_matrix = fix_columns(modified_matrix, row_to_modify, col_int, 
                                        column_list)

    return matrix, 0



# function that will handle if a column says that it should fill all it's rows
def add_all_to_col(matrix, col_to_modify, count_to_modify, column_list, row_list):
    return matrix, 0


def fix_columns(matrix, row_modified, col_modified, column_list):

    return matrix



def fix_rows(matrix, column_modified, row_modified, row_list):
    return matrix