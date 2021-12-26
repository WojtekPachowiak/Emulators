import numpy as np
from memory import Memory as m
# from opcodes import Opcodes as o
from disassembler import Disassembler as d
from opcodes import Opcodes as o



class CPU: #this class's alias is '_'
    
    def list_ops_in_rom(path : str):
        c._load_rom(path)
        while m.PC+1 < len(m.rom): 
            d.disassemble(m.rom[m.PC], m.rom[m.PC+1])
            m.PC += 2
        d.print_used_ops()

    def _load_rom(path : str):
        m.rom = np.fromfile(path, dtype='>u1') # >u2 = uint16 big endian

    def play(rom_path):
        m.memory_reset()
        c._load_rom(rom_path)
        while m.PC+1 < len(m.rom): 
            d.disassemble(m.rom[m.PC], m.rom[m.PC+1])
            o.match_op(m.rom[m.PC], m.rom[m.PC])
            m.PC += 2
        


    # def _read_op():
    #     op = m.rom[m.PC : m.PC+2]
    #     o.opcodes_dict[op]()
    
    # def play(path):
    #     m.reset()
    #     c._load_rom(path)
    #     rom_len = len(m.rom)
    #     while m.PC+1 < rom_len:
    #         op = c._read_op()
    #         c.PC += 2




c = CPU #alias
