n = int(input())
ls = []

for _ in range(n):
    name = input()
    score = float(input())
    ls.append([name, score])

grades = [float(i) for i in x[1:] for x in ls]
grades = list(sorted(grades))
grades = list(filter(min(grades).__ne__, grades))

for i in ls:
    if i[1] == min(grades):
        print(i[0])
