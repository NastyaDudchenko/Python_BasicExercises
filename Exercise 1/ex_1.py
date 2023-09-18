def multi_or_sum(num1, num2):
    multi = num1 * num2
    if multi <= 1000:
        return multi
    else:
        add = num1 + num2
        return add


try:
    print("Enter the first number ")
    number1 = int(input())
except:
    print("Something went wrong!")

try:
    print("Enter the second number ")
    number2 = int(input())
except:
    print("Something went wrong!")

try:
    print("The result is", multi_or_sum(number1, number2))
except:
    print("Wrong input!")