n = int(input())

for i in range(1, n + 1):
    w = len(bin(n)) - 2
    print("{0:{1}d} {0:{1}o} {0:{1}X} {0:{1}b}".format(i, w))
