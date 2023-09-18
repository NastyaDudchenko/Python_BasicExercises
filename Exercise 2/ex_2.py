def sum_current_and_prev_numbers():
    prev_num = 0
    for num in range(10):
        sum = prev_num + num
        print("Current Number", num, "Previous Number", prev_num, "Sum:", sum)
        prev_num = num


print("Printing current and previous number sum in a range(10)")
sum_current_and_prev_numbers()