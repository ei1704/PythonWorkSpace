# P.172
functions = [sum, min, max]
number_list = range(1, 11)
4
for func in functions:
    print("Function: {}, Result: {}".format(func.__name__,
                                            func(number_list)))
    print("Function: {}, Result: {}".format(func, func(number_list)))
# 違いは何か？
