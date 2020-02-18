

# function that will print out our matrix with the row and column numbers included
def print_matrix(matrix, row_list, num_rows, column_list, num_cols):
    row_counter = 0
    col_count = 0

    # print out the numbers for each row
    while row_counter is not len(row_list[0]):
        print(" "*num_cols, end = " ")

        for item in row_list:
            #if item[row_counter] is not 0:
            print(" " + str(item[row_counter]), end = " ")
            #else:
            #    print("  ", end = " ")
        
        print(" ")
        row_counter += 1

        
    column_list_num = 0

    # loop through our columns and rows to print out our matrix
    for row_number in range(num_rows):
        for item in column_list[column_list_num]:
            print(str(item) + " ", end=" ")
            # else:
            #     print("  ", end = " ")

        for col_number in range(num_cols):
            # if column number = 0, print out the column amounts
            print("__", end=" ")
        
        column_list_num += 1
        print("")

    print("\n")



def calculate_nonogram(matrix, row_list, num_rows, column_list, num_cols):
    # get the max amount of items
    # note that since this passes in the equalized cols and rows, we can just use the first
    #       element to calculate this
    max_row_item_amount = len(row_list[0])

    # create variables that will be modified when possibly filling all the rows or columns
    #       of a section of matrix
    num_rows_that_can_be_fill = num_rows
    num_columns_that_can_be_filled = num_cols

    # search through rows to see if any of them are the same length as the column
    for row in range(num_rows):
        for count in range(max_row_item_amount):
            if row_list[row][count] == num_cols:
                matrix, row_list[row][count] = add_all_to_row(matrix, row, count, row_list, column_list)

    print("....solving.....\n")
    print_matrix(matrix, row_list, num_rows, column_list, num_cols)

    # search through columns to see if any of them are the same length as the rows
    for col in range(num_rows):
        for count in range(max_row_item_amount):
            if row_list[col][count] == num_rows:
                matrix, column_list[col][count] = add_all_to_col(matrix, col, count, column_list, row_list)

    print("....solving.....\n")
    print_matrix(matrix, row_list, num_rows, column_list, num_cols)


# function that will handle if a row says to fill all it's columns
def add_all_to_row(matrix, row_to_modify, count_to_modify, row_list, column_list):
    num_to_modify = row_list[row_to_modify][count_to_modify]

    modified_matrix[:] = list(matrix)

    for col_section in matrix[row_to_modify]:
        modified_matrix[row_to_modify][col_section] = "[]"


    for col_int in range(len(row_list)):
        modified_matrix = fix_columns(modified_matrix, row_to_modify, col_int, column_list)

    return modified_matrix, 0



# function that will handle if a column says that it should fill all it's rows
def add_all_to_col(matrix, col_to_modify, count_to_modify, column_list, row_list):
    num_to_modify = column_list[col_to_modify][count_to_modify]

    for row_int in range(len(row_list)):
        matrix = fix_rows(matrix, col_to_modify, row_int, row_list)

    return matrix, 0


def fix_columns(matrix, row_modified, col_modified, column_list):

    return matrix



def fix_rows(matrix, column_modified, row_modified, row_list):
    return matrix