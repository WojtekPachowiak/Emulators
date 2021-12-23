from memory import Memory as m
from disassembler import Disassembler as d
from opcodes import Opcodes as o


class CPU:

    do_disassemble = True

    def run():
        while m.PC < len(m.rom):
            if c.do_disassemble: d.disassemble()
            m.PC += o.match_opcode()

c = CPU