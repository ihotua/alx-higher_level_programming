#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)

    tot_sum = 0
    tot_weight = 0

    for score, weight in my_list:
        tot_sum += score * weight
        tot_weight += weight

    return (tot_sum / tot_weight)
