s = input()

flag1 = flag2 = flag3 = flag4 = flag5 = False
for i in range(len(s)):
    if flag1 and flag2 and flag3 and flag4 and flag5:
        break
    for j in range(i + 1, len(s) + 2):
        if s[i:j].isalnum() and not flag1:
            flag1 = True
        if s[i:j].isalpha() and not flag2:
            flag2 = True
        if s[i:j].isdigit() and not flag3:
            flag3 = True
        if s[i:j].islower() and not flag4:
            flag4 = True
        if s[i:j].isupper() and not flag5:
            flag5 = True

print(flag1, flag2, flag3, flag4, flag5, sep="\n")
