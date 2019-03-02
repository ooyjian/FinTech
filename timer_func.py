import time
import _thread

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


# # This part tests 多线程
# def my_name():
#     while True:
#         time.sleep(7)
#         print("欧宇健")
#
#
# _thread.start_new_thread(time_func, (('3', 'SECONDS'),))
# _thread.start_new_thread(my_name, ())
#
# # Press enter to exit
# input("")