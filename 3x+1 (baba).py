import matplotlib.pyplot as graph

x = []
y = []

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

def drawGraph(x,y):
    global c
    global i
    graph.plot(x,y,color='blue', linewidth=2,marker="o",markersize=5)
    graph.xlabel("Input into Collatz")
    graph.ylabel("Number of Iterations")
    graph.title("Number of Iterations for each Collatz")
    graph.ylim(0,20)
    graph.xlim(0,10)
    graph.show()


for i in range(1,11):
    max = 0
    c = 1
    x.append(i)
    print(f'Collatz for {i}'.format(i))
    currentCollatz = collatz(i)
    while currentCollatz != 1:
        currentCollatz = collatz(currentCollatz)
        max = maxCheck()
        counter()
    y.append(c)
    print(f'Collatz has ended after {c} iterations with a maximum value of {max}')

drawGraph(x,y)