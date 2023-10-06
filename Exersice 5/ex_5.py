def compare_the_first_and_the_last_values(list):
    print("Given list:", list)
    if list[0] == list[- 1]:
        print("Result is TRUE")
    else:
        print("Result is FALSE")


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
compare_the_first_and_the_last_values(numbers_x)
compare_the_first_and_the_last_values(numbers_y)
