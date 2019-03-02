import pandas
import numpy as np

def zscore(input_data):
    """
    Compute the z-score for a group of data
    :param input_data: the input data
    :return: the zscore for the data
    """
    input_data = np.array(input_data)
    # Initialize the z-score list
    zscore = []
    # For each piece of data, compute its z-score
    for i in range(len(input_data)):
        daily_zscore = (input_data[i] - np.mean(input_data))/np.std(input_data)
        zscore.append(daily_zscore)
    return zscore

def fin_advice(zscore):
    """
    This return the advice that whether we should keep the stock, sell it, or buy it
    :param zscore:
    :return:
    """
    if zscore[-1] > 1:
        return "You should sell"
    elif zscore[-1] < -1:
        return "You should buy"
    else:
        return "You should keep"