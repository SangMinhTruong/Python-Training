n = int(input())
ls = []

for _ in range(n):
    name = input()
    score = float(input())
    ls.append([name, score])

grades = [float(i) for x in ls for i in x[1:]]
grades = list(sorted(grades))
grades = list(filter(min(grades).__ne__, grades))

ls = list(sorted(ls))

for i in ls:
    if i[1] == min(grades):
        print(i[0])
