# Insertion sort algorithm 
# O(n^2) time complexity
# added space complexity of O(n) for list --> not in place sorting
# best case time complexity of O(n) when the list is already sorted
# worst case time complexity of O(n^2) when the list is sorted in reverse order
# average case time complexity of O(n^2) when the list is randomly sorted
# is stable sort algorithm --> values of equal elements not rearranged in the sorted list

numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
sorted = []

for num in numbers:
    if len(sorted) == 0:
        sorted.append(num)
    else:
        for i in range(len(sorted)):
            if num < sorted[i]:
                sorted.insert(i, num)
                break
            elif i == len(sorted) - 1:
                sorted.append(num)


print(sorted)

