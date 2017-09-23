n = int(input())
t = ()

for i in range(n):
    j = int(input())
    t = t + (j,)

print(hash(t))
