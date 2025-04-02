def fun1(n):
    if n == 0 or n == 1:
        return n
    return fun1(n-2) + fun1(n-1)


call = fun1(9)
print(call)
