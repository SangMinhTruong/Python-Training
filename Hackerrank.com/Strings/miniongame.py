s = input()
consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
vowels = 'UEOAI'

d = {"Stuart":0, "Kevin":0}

for i in range(len(s)):
    if s[i] in consonants:
        d["Stuart"] += len(s) - (i + 1) + 1
    elif s[i] in vowels:
        d["Kevin"] += len(s) - (i + 1) + 1

if d["Stuart"] > d["Kevin"]:
    print("Stuart", d["Stuart"])
elif d["Stuart"] < d["Kevin"]:
    print("Kevin", d["Kevin"])
else:
    print("Draw")
