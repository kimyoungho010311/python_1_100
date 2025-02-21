# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num * num for num in numbers]
# print(squared_numbers)


# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(num) for num in list_of_strings]
# result = [num for num in numbers if num % 2 == 0 and num != 0]
# print(result)

with open('file1.txt', 'r',) as f:
    file1 = [int(line.strip()) for line in f.readlines()]
print(file1)

with open('file2.txt','r') as f:
    file2 = [int(line.strip()) for line in f.readlines()]
print(file2)

result = [num for num in file1 if num in file2]

print(result)
