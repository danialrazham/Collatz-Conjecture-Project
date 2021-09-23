import matplotlib.pyplot as graph

x = []          #Collatz inputs
y = []          #Maximum values
primes = []     #List of prime max numbers in all iterations

def counter():
    global c
    c += 1
    return c


def collatz(i):
    if (i % 2) != 0:
        i = 3*i + 1
        print(i)
    else:
        i = i//2
        print(i)
    return i

def maxCheck():
    global max
    if currentCollatz > max:
        max = currentCollatz
    return max

def drawGraph(x,y):
    global c
    global i
    graph.plot(x,y,color='red', linewidth=2,marker="o",markersize=5)
    graph.xlabel("Input into Collatz")
    graph.ylabel("Max Number")
    #graph.ylabel("Number of Iterations")
    graph.title("Max Numbers for each Collatz")
    #graph.title("Number of Iterations of each Collatz")
    graph.show()

def PrimeCheck(li):
    global y
    global primes
    for i in li:
        if i > 1:
            for d in range(2, i):
                if (i % d) == 0:
                    #print(f'{i} is not a prime')
                    break
                else:
                    #print(f'{i} is a prime')
                    primes.append(i)
    return primes


for i in range(4000,4700):
    max = 0
    c = 1
    x.append(i)
    print(f'Collatz for {i}'.format(i))
    currentCollatz = collatz(i)
    max = maxCheck()
    while currentCollatz != 1:
        currentCollatz = collatz(currentCollatz)
        max = maxCheck()
        counter()
    y.append(max)
    print(f'Collatz has ended after {c} iterations with a maximum value of {max}')

print(y)
lprimes = PrimeCheck(x)
print('')
print(lprimes)
drawGraph(x,y)