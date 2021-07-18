from Led import Led
from effects import *


if __name__ == "__main__":
    led = Led(25, 200)
    delay = 25
    
    a = ef1(led, delay)
    b = ef2(led, delay)
    c = ef3(led, delay)
    while True:
        a.__next__()
        b.__next__()
        # c.__next__()
    
    # for _ in ef2(led):
    #     pass

    # for _ in ef3(led,10):
    #     pass
