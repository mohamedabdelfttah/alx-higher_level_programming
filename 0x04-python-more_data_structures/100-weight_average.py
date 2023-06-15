#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weighte_sum = sum(score * weight for score, weight in my_list)
    t_weight = sum(weight for _, weight in my_list)
    return weighte_sum / t_weight
