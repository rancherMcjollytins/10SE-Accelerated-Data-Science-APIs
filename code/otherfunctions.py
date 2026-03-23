import time
def slow_print(textitem, endval):
    for i in textitem:
        print(i, end=endval, flush=True)
        time.sleep(0.05)