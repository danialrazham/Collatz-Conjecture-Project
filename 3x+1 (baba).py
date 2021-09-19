
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

def maxCheck():
    global max
    if currentCollatz > max:
        max = currentCollatz
    return max
     
for i in range(30,51):
    max = 0
    c = 1
    print(f'Collatz for {i}'.format(i))
    currentCollatz = collatz(i)
    while currentCollatz != 1:
        currentCollatz = collatz(currentCollatz)
        max = maxCheck()
        counter()
    print(f'Collatz has ended after {c} iterations with a maximum value of {max}')
      

    
