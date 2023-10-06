list_numbers = [10, 20, 33, 46, 55]
print("Given list:", list_numbers)
print('Divisible by 5:')

result = list()
for number in list_numbers:
    if number % 5 == 0:
        result.append(str(number))
    else:
        continue
print("Divisible by 5:", ', '.join(result))
