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




'''
Problem 3:

Access Codes: Given a list of access codes, and a dictionary with keys as each access code, sum up all the values at each key (given they exist) within the access code list. If the key doesnt exist, do not add to the running total

INPUT: ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'TUV', 'YZ', 'YZ', 'ABC'], {'ABC': 90, 'GHI': 73, 'JKL': 73, 'MNO': 98, 'PQR': 100, 'YZ': 19}

OUTPUT: 562

'''

def access_codes(codes:list, access_dict:dict) -> int:
    res = 0
    for code in codes:
        val = access_dict.get(code, 0)
        res += val
        # for key, val in access_dict.items():
        #     if i == key:
        #         res += val
    return res

assert access_codes(['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'TUV', 'YZ', 'YZ', 'ABC'], {'ABC': 90, 'GHI': 73, 'JKL': 73, 'MNO': 98, 'PQR': 100, 'YZ': 19}) == 562



'''
Problem 4:

Jewels and Stones: You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".



Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0

Example 3:

Input: jewels = "ats", stones = "AAABTsAts"
Output: 3


'''

def jewels_and_stones(jewels:str, stones:str) -> int:
    res = 0

    # for i in jewels:
    #     for a in stones:
    #         if i == a:
    #             res += 1
    j_dict = {j:1 for j in jewels}
    print(j_dict)
    for stone in stones:
        present = j_dict.get(stone, 0)
        res += present
    return res


assert jewels_and_stones(jewels="ats", stones="AAABTsAts") == 3


#
