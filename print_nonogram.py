'''
AUTHOR: Samantha Muellner

DESCRIPTION: File that will print the matrix of our nonogram as needed

VERSION: 1.0.2v
'''

# function that will print out our matrix with the row and column numbers included
def print_matrix(matrix, row_list, num_rows, column_list, num_cols):
    row_counter = 0
    col_count = 0

    # print out the numbers for each row
    while row_counter is not len(row_list[0]):
        print(" " * num_cols, end = " ")

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

