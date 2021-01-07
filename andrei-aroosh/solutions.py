'''
This is a colab workspace for Andrei and Aroosh
'''


'''
Problem 1

Two Sum: Given an array of integers and a target value, return the indicies of the integers in the array that add up to the target value. Return these values in a list.

INPUT: [10, 33, 55, 2, 68, 100], 88

OUTPUT: [1, 2]

'''

def twosum(arr:list, trg:int) -> list:
    for i in range(len(arr)):
        needed_num = trg - arr[i]
        for x in range(i, len(arr)):
            if arr[x] == needed_num:
                return [i,x]








assert twosum([10, 33, 55, 2, 68, 100], 88) == [1, 2]
