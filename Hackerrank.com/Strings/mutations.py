s = input()
fm = [i for i in input().split(" ")]
fm[0] = int(fm[0])

s = s[:fm[0]] + fm[1] + s[fm[0] + 1:]

print(s)
