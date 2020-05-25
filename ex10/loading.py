import time


def ft_progress(lst):
    start_time = time.time()
    for i in lst:
        print("ETA [{:.0%}]".format(i / len(lst)), end='')
        
        print("{:=>4.25s}".format(">"), end='')
        print("]", "{}/{}".format(i + 1,len(lst)), end='')
        print(" | elapsed time {:.2f}s". format(time.time() - start_time))
        yield i + 1

listy = range(200)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print("ret =",ret)
