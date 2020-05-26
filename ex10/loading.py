import time


def ft_progress(lst):
    start_time = time.time()
    iter_time = 0
    for i in lst:
        if (i == 1):
            iter_time = time.time() - start_time
        print("ETA: {:5.2f}".format((len(lst) - i) * iter_time), "[", end='')
        print("{:>4.0%}]".format(i / len(lst)), end='')
        print(" [{:=>{}}{:{}}".format('',
              i*25/len(lst), '>', 25 - i * 25 // len(lst)), end='')
        print("]", "{}/{}".format(i + 1, len(lst)), end='')
        print(" | elapsed time {:.2f}s". format(time.time() - start_time))
        yield i


listy = range(100)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print("ret =", ret)
