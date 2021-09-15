

""" count = 0

def collatz(i):
    if (i % 2) != 0:
        i = 3*i + 1
        print(i)
    else:
        i = i/2
        print(i)
    while i != 2:
        if (i % 2) != 0:
            i = 3*i + 1
            print(i)
        else:
            i = i/2
            print(i)
    print(f'The collatz function ends at {i}'.format(i))
    return i

for i in range(1,10):
    collatz(i)

 """

 








