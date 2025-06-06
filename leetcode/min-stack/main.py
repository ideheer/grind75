import os
import sys

# Get the current directory of the script (subpackage1)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory (my_package)
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)
from solution import *

if __name__ == '__main__':
    # Read data from file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    f = open(f"{current_dir}/data", "r")
    data = f.readlines()
    data = [line.strip() for line in data]

    one_test_number = 3  # It has 3 rows: function, input, output
    if len(data) % one_test_number:
        print("The format of test data is incorrect")
        exit(1)

    all_test = 0
    fail_test = 0
    test_number = len(data) // one_test_number
    for i in range(test_number):
        print(f"Case {i + 1} testing...")
        function_names = split_str_to_func(data[i * one_test_number + 0])
        input_params = split_str_to_params(data[i * one_test_number + 1])
        output_params = split_str_to_params(data[i * one_test_number + 2])

        # The first one is usually initialization
        input_param = split_str_to_params(input_params[0])
        func_num = len(function_names)
        sol: MinStack = MinStack()

        for j in range(1, func_num):
            input_param = split_str_to_params(input_params[j])
            if function_names[j] == "push":
                val: int = convert_params(input_param[0], 'int')
                sol.push(val)
            if function_names[j] == "pop":
                sol.pop()
            if function_names[j] == "top":
                real_res: int = convert_params(output_params[j], 'int')
                my_res: int = sol.top()
                check_result: bool = compare_result(f"{i + 1}-{j}", my_res, real_res, 'int')
                all_test += 1
                if not check_result:
                    fail_test += 1
            if function_names[j] == "getMin":
                real_res: int = convert_params(output_params[j], 'int')
                my_res: int = sol.getMin()
                check_result: bool = compare_result(f"{i + 1}-{j}", my_res, real_res, 'int')
                all_test += 1
                if not check_result:
                    fail_test += 1

    print(f"The number of test cases: {all_test}")
    print(f"The number of test cases failed: {fail_test}")
