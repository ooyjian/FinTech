import collections

import Brief_helper_funcitons

def combining(head, data, tail=None):
    """
    :param head: a head string
    :param data: data which will be added to the string
    :param tail: tail string(optional)
    :return: a combined string with head and data
    """
    string = head
    for company, percentage in data.items():
        string += company + ' with percentage ' + percentage

    return string

def return_brief(companies):
    brief = ""
    rise_comp = Brief_helper_funcitons.return_rise(companies)
    fall_comp = Brief_helper_funcitons.return_fall(companies)
    high_rise_comp = Brief_helper_funcitons.highest_rise(companies)
    high_fall_comp = Brief_helper_funcitons.highest_fall(companies)


    return_rising_string = combining("Rising stocks: ", rise_comp)
    return_falling_string = combining("Falling stocks: ", fall_comp)
    return_high_rise = "Highest rising stock: " + high_rise_comp[0] + " with percentage " + high_rise_comp[1]
    return_high_fall = "Highest falling stock: " + high_fall_comp[0] + " with percentage " + high_fall_comp[1]


    brief = brief + return_rising_string + " " + return_falling_string + " " + return_high_rise + " " + return_high_fall + " " +














