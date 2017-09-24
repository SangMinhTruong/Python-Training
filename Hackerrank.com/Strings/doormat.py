N, M = map(int,input().strip().split(" "))

for i in range(0, (N - 1)//2):
    print("{0:{1}^{2}}".format(".|."*(2*i + 1), "-", M))

print("{0:{1}^{2}}".format("WELCOME", "-", M))

for i in range((N - 1)//2 - 1, -1, -1):
    print("{0:{1}^{2}}".format(".|."*(2*i + 1), "-", M))
