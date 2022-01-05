#!/usr/bin/python3


def weight_average(my_list=[]):
    totalScore = 0
    totalWeight = 0
    for elem in my_list:
        score = elem[0]
        weight = elem[1]
        totalScore += score * weight
        totalWeight += weight
    return totalScore / totalWeight
