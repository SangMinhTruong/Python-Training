s = input()

def swap_case(s):
    swapped = ""

    for c in s:
        if c == c.lower():
            swapped += c.upper()
        else:
            swapped += c.lower()

    return swapped

result = swap_case(s)

print(result)
