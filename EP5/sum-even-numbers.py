input_list = list(map(int, input("Enter a list of integers seperated by spaces: ").split()))

even_numbers = []

for num in input_list:
    if num % 2 == 0:
        even_numbers.append(num)

print(sum(even_numbers))


