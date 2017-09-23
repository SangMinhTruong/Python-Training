y = int(input())

if not (y % 4):
    if not (y % 100) and (y % 400):
        print(False)
    else:
        print(True)
else:
    print(False)
