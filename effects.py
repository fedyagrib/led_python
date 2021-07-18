from Led import Led
from random import randint

def ef1(led:Led, delay):
    clr = [randint(0,255),randint(0,255),randint(0,255)]
    
    while True:
        clr[randint(0,2)] = randint(0,255)
        for i in range(len(led)+1):
            tmp = [c/len(led)*(i+5) for c in clr]
            led[i] = led[len(led)-i] = tmp
            led.show(delay)
            yield

def ef2(led: Led, delay):
    led.array[:,:,:] = 0
    while True:
        pix = randint(0, len(led))
        led.random_clr(pix)
        led.clearing(10)
        led.show(delay)
        yield

def ef3(led: Led, delay):
    led.array[:,:,:] = 0
    while True:
        val = [randint(0,255),randint(0,255),randint(0,255)]
        for i in range(len(led)):
            led[i] = val
            led.clearing(10)
            led.show(delay)
            yield
        val = [randint(0,255),randint(0,255),randint(0,255)]
        for i in reversed(range(len(led))):
            led[i] = val
            led.clearing(10)
            led.show(delay)
            yield