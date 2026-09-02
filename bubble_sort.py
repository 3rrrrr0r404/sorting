# Bubble Sort Algorithm using list
# O(n^2) time complexity
# added space complexity of O(1) for list --> in place sorting
# best case time complexity of O(n) when the list is already sorted
# worst case time complexity of O(n^2) when the list is sorted in reverse order
# average case time complexity of O(n^2) when the list is randomly sorted
# is stable sort algorithm --> values of equal elements not rearranged in the sorted list

numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for num in range(len(numbers)):
    solved = True
    for iterations in range(len(numbers)-1):
        if numbers[iterations] > numbers[iterations + 1]:
            numbers[iterations], numbers[iterations + 1] = numbers[iterations + 1], numbers[iterations]
            solved = False
    if solved:
        break

for num in numbers:
    print(num)

