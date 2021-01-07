import random
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



'''
Problem 2

Clean the noise: Given a string of what is SUPPOSED to be a normal sentence, return the CLEANED version of the sentence. This means that there will be random punctuation inserted in the sentence.

INPUT: "I& #lo!ve% to %c!o%d&e %a@n^d ^c!ol#ab% ^o!n g$i&t@hub# w%ith $m$y& fo@lks!"

OUTPUT: "I love to code and colab on github with my folks"

'''
def clean_string(noisy_str:str) -> str:
    res = ''
    # loop through noisy_str 
    for char in noisy_str:
        # checking whether char is an alphabet
        if char.isalpha() or char == " ": 
            res += char

    return res

assert clean_string("""I& #lo!ve% to %c!o%d&e %a@n^d ^c!ol#ab% ^o!n g$i&t@hub# w%ith $m$y& fo@lks!""") == "I love to code and colab on github with my folks"

