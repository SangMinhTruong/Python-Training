M = int(input())
m = {int(i) for i in input().strip().split(" ")}
N = int(input())
n = {int(i) for i in input().strip().split(" ")}

diff = {i for i in list(m^n)}
for i in range(len(diff)):
    print(list(sorted(diff))[i])
