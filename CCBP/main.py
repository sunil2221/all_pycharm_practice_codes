n = int(input())
length = 2*n
k = n
for i in range(1, length):
    top = "  " * (k - i)
    bottom = "  " * (i - k)
    if i == 1:
        print(top + "# ")
    elif i == length-1:
        print(bottom + "# ")
    elif i > n:
        print(bottom + "+ "*(n-2) + "# ")
        n -= 1
    else:
        print(top + "+ "*(i-1) + "# ")