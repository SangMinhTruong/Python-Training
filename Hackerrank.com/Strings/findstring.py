s = input()
check = input()
counter = 0

for i in range(len(s) - len(check) + 1):
    if s[i:i + len(check)] == check:
        counter += 1

print(counter)
