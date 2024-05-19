from multiprocessing import Process

# Teste 1 - Hello world!
'''
def f(name):
    print('hello, sou',name)

if __name__ == '__main__':
    p = Process(target=f,args=('bob filho', ))
    p.start()
    p.join()
'''

# Teste 2 - Os 4x Hello World!
'''
def f(name, id):
    print('hello, sou', name, id)

if __name__ == '__main__':
    procs = []
    for i in range(4):
        p = Process(target=f, args=('bob filho', i, ))
        procs.append(p)

    print('hello, sou', 'bob pai')
    for i in range(4):
        procs[i].start()
    for i in range(4):
        procs[i].join()
'''

# Teste 3 - PI SEQUENCIAL

import time

def pi_naive(start, end, step):
    print ("Start: ", str(start))
    print ("End: ", str(end))
    sum = 0.0
    for i in range(start, end):
        x = (i+0.5) * step
        sum = sum + 4.0/(1.0+x*x)
    return sum

if __name__ == "__main__":
    num_steps = 10000000 #10.000.000 (10+e7)
    sums = 0.0
    step = 1.0/num_steps
    tic = time.time() # Tempo Inicial
    sums = pi_naive(0, num_steps, step)
    toc = time.time() # Tempo Final
    pi = step * sums
    print ("Valor Pi: %.10f" %pi)
    print ("Tempo Pi: %.8f s" %(toc-tic))
