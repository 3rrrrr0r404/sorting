# Selection Sort Algorithm
# O(n^2) time complexity
# added space complexity of O(1) for list --> in place sorting
# best case time complexity of O(n^2) when the list is already sorted
# worst case time complexity of O(n^2) when the list is sorted in reverse order
# average case time complexity of O(n^2) when the list is randomly sorted
# is not stable sort algorithm --> values of equal elements may be rearranged in the sorted list

numbers = [45, 3, 2, 10, 7, 8, 1, 4, 6, 5]

for num in range(len(numbers)):
    min_num = [numbers[num],num]
    for iterations in range(num, len(numbers)):
        min_num = [numbers[iterations], iterations] if numbers[iterations] < min_num[0] else min_num

    numbers[min_num[1]] = numbers[num]
    numbers[num] = min_num[0]

for i in numbers:
    print(i)

    
