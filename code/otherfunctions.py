import time
def slow_print(textitem):
    for i in textitem:
        print(i, end='', flush=True)
        time.sleep(0.05)