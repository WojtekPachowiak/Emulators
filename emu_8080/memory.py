import numpy as np

class Memory:
    PC = np.uint16()
    SP = np.uint16()

    A = np.uint8() #accumulator
    B = np.uint8()
    C = np.uint8()
    D = np.uint8()
    E = np.uint8()
    H = np.uint8()
    L = np.uint8()

    #FLAGS
    Sign = False 
    Zero = False
    Parity = False
    Carry = False

    memory = None
    rom = None

m = Memory