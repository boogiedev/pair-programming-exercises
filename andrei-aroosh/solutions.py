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
    # print(j_dict)
    for stone in stones:
        present = j_dict.get(stone, 0)
        res += present
    return res


assert jewels_and_stones(jewels="ats", stones="AAABTsAts") == 3



"""
Problem 5:

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i'th customer has in the j'th bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.



Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation:
1st customer has wealth = 6
2nd customer has wealth = 10
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17


"""

def greatest_wealth(accounts:list) -> int:
#     res = []
#     for customer in accounts:
#         res.append(sum(customer))

#     return max(res)

    res = -1
    for customer in accounts:
        account_sum = sum(customer)
#         res = account_sum if account_sum > res else res
        if account_sum > res:
            res = account_sum

    return res



assert greatest_wealth([[2,8,7],[7,1,3],[1,9,5]]) == 17




"""
Problem 6:

Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true

"""


def valid_parentheses(paren_string:str) -> bool:
    dct = {"[": "]", "(": ")", "{" : "}"}
    stack = []
    for char in paren_string:
        if char in dct:
            stack.append(char)
        else:
            if not stack or char != dct[stack.pop()]:
                return False
    return not stack



assert valid_parentheses('()[]{}') == True


"""
Problem 7:

Greatest Number Candies

Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.


Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]

Explanation:
Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids.
Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids.
Kid 3 has 5 candies and this is already the greatest number of candies among the kids.
Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies.
Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids.


Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]
Explanation: There is only 1 extra candy, therefore only kid 1 will have the greatest number of candies among the kids regardless of who takes the extra candy.


Example 3:

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
"""

def kidsWithCandies(candies:list, extraCandies:int) -> list:
    res = []
    max_candies = max(candies)
    for i in candies:
        currentCandies = extraCandies + i
        # if currentCandies >= max_candies:
        #     res.append(True)
        # else:
        #     res.append(False)
        res.append(currentCandies >= max_candies)

    return res

assert kidsWithCandies(candies=[4,2,1,1,2], extraCandies=1) == [True,False,False,False,False]



"""
Problem 8:

Design a Parking System

Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.


Example 1:

Input:
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]

Output:
[null, true, true, false, false]


"""

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int):


        if carType == 1 and self.big > 0:
            self.big -= 1
        if carType == 2 and self.medium > 0:
            self.medium -= 1
        if carType == 3 and self.small > 0:
            self.small -= 1




bellevue_square = ParkingSystem(2, 1, 1)
# This is possible
bellevue_square.addCar(1)
# This is possible
bellevue_square.addCar(2)
# This is NOT possible
bellevue_square.addCar(2)

print(bellevue_square.small)
print(bellevue_square.medium)
print(bellevue_square.big)
