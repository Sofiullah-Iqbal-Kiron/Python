T = int(input())
for i in range(0, T, 1):
    N = input()
    if (i == T - 1):
        print("sum =", int(N[0]) + int(N[4]), end="")
    else:
        print("sum =", int(N[0]) + int(N[4]))
