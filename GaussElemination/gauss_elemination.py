# solves system of linear equations
# we approach the gauss elemination methode
# hence we need matrices formed by those system of equation
# we directly put here the matirx and solve for the variables


import numpy as np


def main():
    a = np.array([[2, 1, 1, 10], [3, 2, 3, 18], [1, 4, 9, 16]])
    d = get_variable(variable_elemination(a))
    for i in range(1, len(d) + 1):
        print(f"x_{i}: ", sep="", end="")
        print(d[-i])


def variable_elemination(arr):
    """
    this function creates a dictionary of matrices eleminating variables
    """
    variable_num = len(arr[0]) - 1
    equations = len(arr[0:, 0])
    # we'll put arrays into a dictonary after the whole dimention elemination
    arr_dic = {1: arr}  # put perfect array
    for i in range(variable_num):
        temp_list = [arr[0]]  # to transform list to array
        for j in range(len(arr[0:, 0]) - 1):
            row_elemination = np.array(
                arr[0] * (-arr[j + 1, 0] / arr[0, 0]) + arr[j + 1]
            )
            temp_list.append(row_elemination)
        arr = np.array(temp_list)
        arr_dic[i + 1] = arr
        # reshaping arr
        arr = arr[1:]
        ayy = []  # new arr as list
        for item_arr in arr:
            axx = np.delete(item_arr, 0)  # deleted 1st item from each row
            ayy.append(axx)
        arr = np.array(ayy)
    return arr_dic


def get_variable(d):
    """
    returns roots in listed form
    """
    variables_with_real_value = []
    for i in reversed(range(1, len(d) + 1)):  # proper array execution
        real_time_arr = d[i][0]
        variable = real_time_arr[-1] / real_time_arr[0]
        # print(variable)
        if len(real_time_arr) == 2:
            variables_with_real_value.append(variable)  # creating dic...
        elif len(real_time_arr) > 2:
            temp_l = []
            i = 1
            for k in range(1, len(real_time_arr) - 1):
                temp_variable = (
                    real_time_arr[k] * variables_with_real_value[-i]
                )  # before subtraction
                i = i + 1
                temp_l.append(temp_variable)
            variable1 = (real_time_arr[-1] - sum(temp_l)) / real_time_arr[0]
            variables_with_real_value.append(variable1)
    return variables_with_real_value


if __name__ == "__main__":
    try:
        main()
    except IndexError:
        print("Check your mattrix...")
