import time

def time_func(interval):
    """
    Send the information about stock price every interval seconds
    :param interval: the length of the interval in seconds
    :return: None
    """
    for i in range(3):
        time.sleep(interval)
        print("Hello World!")

time_func(30)
