#mergesort
#recursive sorting algorithm using divide and conquer
#O(n log n) time complexity
#best case: O(n log n) when the list is already sorted
#worst case: O(n log n) when the list is sorted in reverse order
#average case: O(n log n)
#added space complexity: O(n) --> not in place sorting
#is stable sorting algorithm --> values of equal elements stay in order

#list is broken in half, down into smaller sublists
#when lists are 1 / 0 in length, they are merged back together
#left and right sublists are compared iteratively and merged in sorted order
#each merge has n comparisons
# there are log n merges, therefore O(n log n) time complexity regardless of order
#works because each sublist is sorted before merging
#therefore, sublists already in ascending order
#works well for large lists, but not as fast as quicksort for small lists 


def split(arr):
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:]

    return left, right



def merge(left, right):
    result = []
    pointer_left = 0
    pointer_right = 0

    while pointer_left < len(left) and pointer_right < len(right):
        if left[pointer_left] < right[pointer_right]:
            result.append(left[pointer_left])
            pointer_left +=1
        else:
            result.append(right[pointer_right])
            pointer_right += 1

    while pointer_left < len(left):
        result.append(left[pointer_left])
        pointer_left += 1
    while pointer_right < len(right):
        result.append(right[pointer_right])
        pointer_right += 1

    return result

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    else:
        left, right = split(arr)

        left = mergesort(left)
        right = mergesort(right)

        return merge(left, right)

numbers = [10, 5, 2, 3, 7, 1, 9, 4, 6, 8]
sorted_numbers = mergesort(numbers)
print(sorted_numbers)
