# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:15:49 2019

@author: aseal
"""

def edu(eth,gender,status,fr_count,sex,tenure,pop,post_count):
    if gender == "f" and sex == "straight":
        if tenure <= 12:
            if pop == "<50000":

            elif pop == "1mil-5mil":
                print("bachelors")
            elif pop == "50000-100000":
                print("High School")
    elif tenure <= 9:
        print("High School")
    else:
        print("Masters")