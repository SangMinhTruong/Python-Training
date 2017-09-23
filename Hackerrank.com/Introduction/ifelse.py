n = int(input())
if not (n % 2):
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")
