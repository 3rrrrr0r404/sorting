# Note: this is like outstanding scholarship level stuff
#  QuickSort 
# O(n log n) time complexity on average
# added space complexity of O(n) for list --> not in place sorting
# best case time complexity of O(n log n) when the list is already sorted
# worst case time complexity of O(n^2) when the list is sorted in reverse order
# not stable sort algorithm --> values of equal elements may be rearranged in the sorted list


# is a recursive algorithm that uses a divide-and-conquer approach
# list is broken down into smaller sublists around a pivot
# the pivot is the last element of the list
# elements in sublists are moved left or right of the pivot based on their value
# this is repeated until sublists are 1 or 0 in length
#then sublists are combined together to make sorted list


def quicksort(arr):

    # the base case is when len(arr) <=1
    #i.e list with 0 or 1 element == already sorted

    if len(arr) <= 1:
        return arr

    #setting the last element of the list as the pivot

    pivot = arr[-1]

    #this is short hand for creating a new list
    # it uses shorthand for loop and if statment

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    #long hand would be:
    # left = right = []
    # for x in arr[:-1]:
    #     if x <= pivot:
    #         left.append(x)
    #     else:
    #         right.append(x)   


    #recursively call the function based on sublists made
    #and return the combined sorted list
    #note: we are concatinating lists, so pivot must be in square brackets

    return quicksort(left) + [pivot] + quicksort(right)


#main working area

unsorted_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#calling the function
sorted_list = quicksort(unsorted_list)
print(sorted_list)