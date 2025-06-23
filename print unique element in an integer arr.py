# print unique element in an integer array print unique element

# or find print distinct element array

def Print_Unique_Elements(numbers)-> int:

    for read_index in range(0, len(numbers), 1):

        isDuplicate = False

        for compare_index in range(0, len(numbers), 1):

            if read_index == compare_index:

                continue

            if numbers[read_index] == numbers[compare_index]:

                isDuplicate = True

                break

        if (isDuplicate == False):

            # this is unique element henece print numbers

            print(numbers[read_index])


def invoke_Print_Unique_Elements():

   # input1 = [1,2,3,1,4]

    input1 = [1,2,3,4,5]

    Print_Unique_Elements(input1)

# invocation code

invoke_Print_Unique_Elements()