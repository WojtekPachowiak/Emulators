import numpy as np

class Memory:
    memory = np.zeros(4096, dtype = np.uint8)
    rom_address = 0x200
    V = np.uint8(0) #general purpose
    I = np.uint16(0) #general purpose
    PC = np.uint16(0) #program counter
    SP = np.uint8(0) #stack pointer
    DT = np.uint8(0) #delay timer
    ST = np.uint8(0) #sound timer

    rom = None #variable for storing rom data (np.array) 
    op = None 

    def reset():
        _.V = np.uint8(0) 
        _.I = np.uint16(0) 
        _.PC = np.uint16(0) 
        _.SP = np.uint8(0) 
        _.DT = np.uint8(0) 
        _.ST = np.uint8(0) 
        _.rom = None



_ = Memory