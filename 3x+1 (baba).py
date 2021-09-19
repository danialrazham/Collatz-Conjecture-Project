
def collatz(i):
    c = 0
    if (i % 2) != 0:
        i = 3*i + 1
        c += 1
        print(i)
    else:
        i = i/2
        print(i)
        c += 1
    while i != 1:
        if (i % 2) != 0:
            i = 3*i + 1
            c += 1
            print(i)
        else:
            i = i/2
            c += 1
            print(i)
    print(f'The collatz function ends at {i} after {c} iterations')
    
for i in range(1,10):
    max=0
    print(f'collatz for {i}'.format(i))
    currentcollatz=collatz(i)
    if currentcollatz > max:
        max=currentcollatz  
    print(max)



""" def counter():
    global c
    c += 1
    return c """
    


""" def collatz(i):
    if (i % 2) != 0:
        i = 3*i + 1
        print(i)
    else:
        i = i/2
        print(i)
    return i

def maxCheck():
    
     
for i in range(1,11):
    c = 1
    print(f'Collatz for {i}'.format(i))
    i = collatz(i)
    while i != 1:
        i = collatz(i)
        counter()
    print(f'Collatz has ended at {i} after {c} iterations')
      

    

for i in range(1,10):
    print(f'collatz for {i}'.format(i))
    collatz(i)
    if i != 2:
        collatz(i)
    else:
        print(f'collatz has ended at {i}') """