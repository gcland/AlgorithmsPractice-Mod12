# Problem statement: 
# Given a list (array) of integers, consider a sorting algorithm that arranges the list in ascending order.
# - Use the Insertion Sort Algorithm. Calculate the Big O Complexity of the algorithm. Assess the efficiency of algorithm.
# -------------------------------------------------------------------------------------------------
# 
# 

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1

        while j >=0 and key < array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1]=key
    return array

array = [10, 5, 6, 2, 11, 21, 33, 43, 34, 50]
print(insertion_sort(array))
