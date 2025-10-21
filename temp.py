# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def is_even(n):
    return n%2 == 0

def get_odds(nums):
    odds = []
    for num in nums:
        if not is_even(num):
            odds.append(num)
        return odds
    my_list = [1, 2, 6, 8, 2, 5, 3]
    my_odds = get_odds(my_list)
    print(len(my_odds))
