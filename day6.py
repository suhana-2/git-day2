def print_numbers(nums):
    for x in nums:
        print(x)

numbers = [1, 2, 3, 4]
print_numbers(numbers)

def find_sum(nums):
    total = 0
    for x in nums:
        total = total + x
    return total

numbers = [1, 2, 3, 4]
result = find_sum(numbers)
print(result)
