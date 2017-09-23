n = int(input())
ls = [int(i) for i in input().strip().split(" ")]
nearmax = min(ls)

for i in range(n):
    if ls[i] < max(ls) and ls[i] > nearmax:
        nearmax = ls[i]

print(nearmax)
