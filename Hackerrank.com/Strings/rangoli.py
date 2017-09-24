ls = [None, "a","b","c","d","e","f","g","h","i","j","k","l","m"
     ,"n","o","p","q","r","s","t","u","v","w","x","y","z"]

n = int(input())
h = n*2 - 1
w = n*2 - 1 + (n*2 - 1 - 1)

for i in range(n, 0, -1):
    s = ls[i]
    for j in range(i + 1, n + 1):
        s = ls[j] + "-" + s + "-" + ls[j]
    print("{0:{1}^{2}}".format(s, "-", w))

for i in range(2, n + 1):
    s = ls[i]
    for j in range(i + 1, n + 1):
        s = ls[j] + "-" + s + "-" + ls[j]
    print("{0:{1}^{2}}".format(s, "-", w))
