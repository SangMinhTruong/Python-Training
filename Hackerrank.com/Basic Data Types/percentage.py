n = int(input())
dic = {}

for i in range(n):
    ls = [i for i in input().strip().split(" ")]
    dic[ls[0]] = list(map(float, ls[1:]))

name = input()
result = sum(dic[name])/len(dic[name])
print("{0:.2f}".format(result))
