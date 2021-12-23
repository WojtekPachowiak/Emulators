import numpy as np
from memory import Memory
from opcodes import Opcodes

m = Memory
o = Opcodes

class CHIP8: #this class's alias is '_'
    
    def _load_rom(path : str):
        m.rom = np.fromfile(path, dtype='uint8')

    def _read_op():
        op = m.rom[m.PC : m.PC+2]
        o.opcodes_dict[op]()
    
    def play(path):
        m.reset()
        c._load_rom(path)
        rom_len = len(m.rom)
        while m.PC != rom_len:
            op = c._read_op()
            c.PC += 2




c = CHIP8 #alias
