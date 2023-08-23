def fib1():
    n0 = 1
    n1 = 1

    print(n0, n1, end=" ")

    for i in range(32 - 2):
        n0 += n1

        # Switcharoo
        temp = n0
        n0 = n1
        n1 = temp

        print(n1, end=" ")
    
    print('\n')

def fib2():
    n0 = 1
    n1 = 1

    #print(n0, n1, end=" ")

    for i in range(79 - 2):
        n0 += n1

        # Switcharoo
        temp = n0
        n0 = n1
        n1 = temp

        if n1 % 2 == 0:
            print(n1, end=" ")

    print('\n')

def fib3():
    n0 = 1
    n1 = 1

    # print(n0, n1, end=" ")

    for i in range(51 - 2):
        n0 += n1

        # Switcharoo
        temp = n0
        n0 = n1
        n1 = temp

        if (n1 % 2 == 0) and (n1 % 3 == 0):
            print(n1, end=" ")

    print('\n')

def fib4():
    n0 = 1
    n1 = 1

    # print(n0, n1, end=" ")

    i = 0
    while i < 10:
        n0 += n1

        # Switcharoo
        temp = n0
        n0 = n1
        n1 = temp

        if (n1 % 2 == 0) or (n1 % 5 == 0):
            print(n1, end=" ")
            i += 1

    print('\n')

fib1()
fib2()
fib3()
fib4()