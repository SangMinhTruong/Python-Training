n = int(input())
ls =[]

for i in range(n):
    cmds = [j for j in input().strip().split(" ")]
    if cmds[0] == "print":
        eval(cmds[0] + "(ls)")
    elif cmds[0] == "insert":
        eval("ls." + cmds[0] + "(" + cmds[1] + ", " + cmds[2] + ")")
    elif cmds[0] in ("remove", "append", "extend", "count", "index"):
        eval("ls." + cmds[0] + "(" + cmds[1] + ")")
    else:
        eval("ls." + cmds[0] + "()")
