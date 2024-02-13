def solve (a, b):
    if a == 0:
        print(b)
    else:
        solve (b % a, a)

solve(20, 50)