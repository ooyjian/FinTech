import time

def time_func(interval):
    """
    Send the information about stock price every interval seconds
    :param interval: a tuple that is in the form of ('time length', 'time unit')
    :return: None
    """
    # Compute how many seconds are there in the interval
    time_length = float(interval[0])
    if interval[1] == str.capitalize("hours") or interval[1] == str.capitalize("hour"):
        interval = time_length * 3600
    elif interval[1] == str.capitalize("minutes") or interval[1] == str.capitalize("minute"):
        interval = time_length * 60
    else:
        interval = time_length
    while True:
        time.sleep(interval)
        print("Hello World!")
