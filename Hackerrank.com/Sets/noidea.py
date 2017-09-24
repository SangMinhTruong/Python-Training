n, m = [int(i) for i in input().strip().split(" ")]
ls = list(map(int, input().strip().split(" ")))
a = {int(i) for i in input().strip().split(" ")}
b = {int(i) for i in input().strip().split(" ")}

scores = [1 if i in a else -1 if i in b else 0 for i in ls]

print(sum(scores))
