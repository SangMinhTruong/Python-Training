def list_append(list, item):
    list.append(item)
    return item

S, N = input(), int(input())
for part in zip(*[iter(S)] * N):
    tmp = []
    print(''.join([list_append(tmp, i) for i in part if i not in tmp]))
