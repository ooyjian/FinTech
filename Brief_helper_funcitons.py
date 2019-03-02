import pandas
import numpy as np

def return_rise(companies):
    """

    :param companies: given dictionary
    :return: companies that have rise in stock price percentage
    """
    rise_company_and_percentrage = {}
    for company, data in companies.items():
        if data[0]>0:
            rise_company_and_percentrage[company] = data[0]
    return rise_company_and_percentrage

def return_fall(companies):
    """

    :param companies: given dictionary
    :return: companies that have fall in stock price percentage
    """
    fall_company_and_percentrage = {}
    for company, data in companies.items():
        if data[0] < 0:
            fall_company_and_percentrage[company] = data[0]
    return fall_company_and_percentrage

def highest_rise(rise_company):
    """

    :param rise_company: dictionary result from return_rise
    :return: the highest rise company
    """
    max = 0
    max_company = None
    for company, percentage in rise_company.items():
        if percentage > max:
            max = percentage
            max_company = company
    return (max_company, max)

def highest_fall(fall_company):
    """

    :param rise_company: dictionary result from return_fall
    :return: the highest fall company
    """
    min = 0
    min_company = None
    for company, percentage in fall_company.items():
        if percentage < min:
            min = percentage
            min_company = company
    return (min_company, min)

def month_average(companies):
    """
    compute monthly average for each company
    :param companies: given dictionary
    :return: a dictionary where key is name of the company and value is the average stock price
    """
    company_average = {}
    for company, data in companies.items():
        sum = 0
        for price in data[1]:
            sum += price
        company_average[company] = sum/len(data[1])

    return company_average