import numpy as np

class Memory:
    memory = np.zeros(4096, dtype = np.uint8)

    #addresses
    addr = {
        "start" : 0x200,
        "screen" : 0xF00,
        "stack" : 0xEA0,
        "fonts" : 0x0
    }
    

    display = np.zeros((64,32), dtype=np.uint8)

    V = np.zeros(16, dtype = np.uint8)
    I = np.uint16(0) 
    PC = np.uint16(0) #program counter
    SP = np.uint8(0) #stack pointer


    #timers
    DT = np.uint8(0) #delay timer
    ST = np.uint8(0) #sound timer

    rom = None #variable for storing rom data (np.array) 


    fonts = np.array([
        0b01100000,
        0b10010000,
        0b10010000,
        0b10010000,
        0b01100000,

        0b01100000,
        0b00100000,
        0b00100000,
        0b00100000,
        0b01110000,

        0b11100000,
        0b00010000,
        0b00110000,
        0b01100000,
        0b11110000,

        0b11100000,
        0b00010000,
        0b01100000,
        0b00010000,
        0b11100000,

        0b10100000,
        0b10100000,
        0b11100000,
        0b00100000,
        0b00100000,

        0b11110000,
        0b10000000,
        0b11110000,
        0b00010000,
        0b11110000,

        0b10000000,
        0b10000000,
        0b11110000,
        0b10010000,
        0b11110000,

        0b11110000,
        0b00010000,
        0b00100000,
        0b00100000,
        0b00100000,

        0b11110000,
        0b10010000,
        0b11110000,
        0b10010000,
        0b11110000,

        0b11110000,
        0b10010000,
        0b11110000,
        0b00010000,
        0b00010000,

        0b01100000,
        0b10010000,
        0b11110000,
        0b10010000,
        0b10010000,

        0b10000000,
        0b10000000,
        0b11110000,
        0b10010000,
        0b11110000,

        0b11110000,
        0b10000000,
        0b10000000,
        0b10000000,
        0b11110000,

        0b11100000,
        0b10010000,
        0b10010000,
        0b10010000,
        0b11100000,

        0b11110000,
        0b10000000,
        0b11100000,
        0b10000000,
        0b11110000,

        0b11110000,
        0b10000000,
        0b11100000,
        0b10000000,
        0b10000000
    ], dtype = np.uint8)

    def memory_reset():
        m.memory = np.zeros(4096, dtype = np.uint8)
        m.V = np.zeros(16, dtype = np.uint8)
        m.I = np.uint16(0)
        m.PC = np.uint16(0) #program counter
        m.SP = np.uint8(0) #stack pointer
        m.DT = np.uint8(0) #delay timer
        m.ST = np.uint8(0) #sound timer
        m.rom = None

    


m = Memory