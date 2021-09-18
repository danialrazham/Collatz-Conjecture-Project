
""" def collatz_whole(i):
    global c
    if (i % 2) != 0:
        i = 3*i + 1
        c += 1
        print(i)
    else:
        i = i/2
        print(i)
        c += 1
    while i != 2:
        if (i % 2) != 0:
            i = 3*i + 1
            c += 1
            print(i)
        else:
            i = i/2
            c += 1
            print(i)
    print(f'The collatz function ends at {i} after {c} iterations')
    return i """
  ###################################################################################################################################  


""" for i in range(1,10):
    print(f'collatz for {i}'.format(i))
    collatz_whole(i)  
 """

c = 0
def counter():
    global c
    c += 1
    return c
    

def collatz(i):
    if (i % 2) != 0:
        i = 3*i + 1
        print(i)
    else:
        i = i/2
        print(i)
    return i

        
for i in range(1,10):
    print(f'Collatz for {i}'.format(i))
    collatz(i)
    counter()
    while i != 2:
        collatz(i)
        counter()
    else:
        print(f'collatz ends at {i} after {c} iterations')
    

