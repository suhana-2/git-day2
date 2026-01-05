def count_items(items):
    count = 0
    for x in items:
        count = count + 1
    return count

numbers = [10, 20, 30, 40]
result = count_items(numbers)
print(result)
