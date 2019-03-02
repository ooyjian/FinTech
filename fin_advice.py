import pandas
import numpy as np

def compute_increase_rate(input_data):
    """
    This function computes the increase rate for the input data
    :param input_data: a dictionary that contains the stock prices for each company
    :return: a list that contains the increasing rate of stock price every day
    """
    rates = {}
    for comp in input_data:
        stock_prices = input_data[comp][1]
        rates[comp] = []
        for i in range(len(stock_prices)-1):
            # Add a new increase rate to the dictionary
            rates[comp].append((stock_prices[i] - stock_prices[i+1])/stock_prices[i+1])
    return rates


def compute_zscore(input_data, comp_name):
    """
    Compute the z-score for a group of data
    :param input_data: the rate the stock prices increase for every day
           comp_name: the name of the company
    :return: the zscore for the data
    """
    try:
        input_data = np.array(input_data[comp_name])
    except KeyError:
        print("The company is not included in our database")
        return False
    # Initialize the z-score list
    zscore = []
    # For each piece of data, compute its z-score
    for i in range(len(input_data)):
        daily_zscore = (input_data[i] - np.mean(input_data))/np.std(input_data)
        zscore.append(daily_zscore)
    return zscore

def fin_advice(input_data, comp_name):
    """
    This return the advice that whether we should keep the stock, sell it, or buy it
    :param input_data: Alex's style of data for the company
           comp_name: the name of the company
    :return: What should the user do to their stock
    """
    # Compute the Z-score for a certain company
    inc_rate = compute_increase_rate(input_data)
    zscore = compute_zscore(inc_rate, comp_name)
    if zscore == False:
        return None
    if zscore[-1] > 1:
        return "You should sell"
    elif zscore[-1] < -1:
        return "You should buy"
    else:
        return "You should keep"