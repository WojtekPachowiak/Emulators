import numpy as np
from memory import Memory as m

class Opcodes:

    def match_opcode(byte):
        match byte:
            case 0x00: return 0
            case 0x01: return 0
            case 0x02: return 0
            case 0x03: return 0
            case 0x04: return 0
            case 0x05: return 0
            case 0x06: return 0
            case 0x07: return 0
            case 0x08: return 0
            case 0x09: return 0
            case 0x0a: return 0
            case 0x0b: return 0
            case 0x0c: return 0
            case 0x0d: return 0
            case 0x0e: return 0
            case 0x0f: return 0
            case 0x10: return 0
            case 0x11: return 0
            case 0x12: return 0
            case 0x13: return 0
            case 0x14: return 0
            case 0x15: return 0
            case 0x16: return 0
            case 0x17: return 0
            case 0x18: return 0
            case 0x19: return 0
            case 0x1a: return 0
            case 0x1b: return 0
            case 0x1c: return 0
            case 0x1d: return 0
            case 0x1e: return 0
            case 0x1f: return 0
            case 0x20: return 0
            case 0x21: return 0
            case 0x22: return 0
            case 0x23: return 0
            case 0x24: return 0
            case 0x25: return 0
            case 0x26: return 0
            case 0x27: return 0
            case 0x28: return 0
            case 0x29: return 0
            case 0x2a: return 0
            case 0x2b: return 0
            case 0x2c: return 0
            case 0x2d: return 0
            case 0x2e: return 0
            case 0x2f: return 0
            case 0x30: return 0
            case 0x31: return 0
            case 0x32: return 0
            case 0x33: return 0
            case 0x34: return 0
            case 0x35: return 0
            case 0x36: return 0
            case 0x37: return 0
            case 0x38: return 0
            case 0x39: return 0
            case 0x3a: return 0
            case 0x3b: return 0
            case 0x3c: return 0
            case 0x3d: return 0
            case 0x3e: return 0
            case 0x3f: return 0
            case 0x40: return 0
            case 0x41: return 0
            case 0x42: return 0
            case 0x43: return 0
            case 0x44: return 0
            case 0x45: return 0
            case 0x46: return 0
            case 0x47: return 0
            case 0x48: return 0
            case 0x49: return 0
            case 0x4a: return 0
            case 0x4b: return 0
            case 0x4c: return 0
            case 0x4d: return 0
            case 0x4e: return 0
            case 0x4f: return 0
            case 0x50: return 0
            case 0x51: return 0
            case 0x52: return 0
            case 0x53: return 0
            case 0x54: return 0
            case 0x55: return 0
            case 0x56: return 0
            case 0x57: return 0
            case 0x58: return 0
            case 0x59: return 0
            case 0x5a: return 0
            case 0x5b: return 0
            case 0x5c: return 0
            case 0x5d: return 0
            case 0x5e: return 0
            case 0x5f: return 0
            case 0x60: return 0
            case 0x61: return 0
            case 0x62: return 0
            case 0x63: return 0
            case 0x64: return 0
            case 0x65: return 0
            case 0x66: return 0
            case 0x67: return 0
            case 0x68: return 0
            case 0x69: return 0
            case 0x6a: return 0
            case 0x6b: return 0
            case 0x6c: return 0
            case 0x6d: return 0
            case 0x6e: return 0
            case 0x6f: return 0
            case 0x70: return 0
            case 0x71: return 0
            case 0x72: return 0
            case 0x73: return 0
            case 0x74: return 0
            case 0x75: return 0
            case 0x76: return 0
            case 0x77: return 0
            case 0x78: return 0
            case 0x79: return 0
            case 0x7a: return 0
            case 0x7b: return 0
            case 0x7c: return 0
            case 0x7d: return 0
            case 0x7e: return 0
            case 0x7f: return 0
            case 0x80: return o.ADD(m.B) 
            case 0x81: return 0
            case 0x82: return 0
            case 0x83: return 0
            case 0x84: return 0
            case 0x85: return 0
            case 0x86: return 0
            case 0x87: return 0
            case 0x88: return 0
            case 0x89: return 0
            case 0x8a: return 0
            case 0x8b: return 0
            case 0x8c: return 0
            case 0x8d: return 0
            case 0x8e: return 0
            case 0x8f: return 0
            case 0x90: return 0
            case 0x91: return 0
            case 0x92: return 0
            case 0x93: return 0
            case 0x94: return 0
            case 0x95: return 0
            case 0x96: return 0
            case 0x97: return 0
            case 0x98: return 0
            case 0x99: return 0
            case 0x9a: return 0
            case 0x9b: return 0
            case 0x9c: return 0
            case 0x9d: return 0
            case 0x9e: return 0
            case 0x9f: return 0
            case 0xa0: return 0
            case 0xa1: return 0
            case 0xa2: return 0
            case 0xa3: return 0
            case 0xa4: return 0
            case 0xa5: return 0
            case 0xa6: return 0
            case 0xa7: return 0
            case 0xa8: return 0
            case 0xa9: return 0
            case 0xaa: return 0
            case 0xab: return 0
            case 0xac: return 0
            case 0xad: return 0
            case 0xae: return 0
            case 0xaf: return 0
            case 0xb0: return 0
            case 0xb1: return 0
            case 0xb2: return 0
            case 0xb3: return 0
            case 0xb4: return 0
            case 0xb5: return 0
            case 0xb6: return 0
            case 0xb7: return 0
            case 0xb8: return 0
            case 0xb9: return 0
            case 0xba: return 0
            case 0xbb: return 0
            case 0xbc: return 0
            case 0xbd: return 0
            case 0xbe: return 0
            case 0xbf: return 0
            case 0xc0: return 0
            case 0xc1: return 0
            case 0xc2: return 0
            case 0xc3: return 0
            case 0xc4: return 0
            case 0xc5: return 0
            case 0xc6: return 0
            case 0xc7: return 0
            case 0xc8: return 0
            case 0xc9: return 0
            case 0xca: return 0
            case 0xcb: return 0
            case 0xcc: return 0
            case 0xcd: return 0
            case 0xce: return 0
            case 0xcf: return 0
            case 0xd0: return 0
            case 0xd1: return 0
            case 0xd2: return 0
            case 0xd3: return 0
            case 0xd4: return 0
            case 0xd5: return 0
            case 0xd6: return 0
            case 0xd7: return 0
            case 0xd8: return 0
            case 0xd9: return 0
            case 0xda: return 0
            case 0xdb: return 0
            case 0xdc: return 0
            case 0xdd: return 0
            case 0xde: return 0
            case 0xdf: return 0
            case 0xe0: return 0
            case 0xe1: return 0
            case 0xe2: return 0
            case 0xe3: return 0
            case 0xe4: return 0
            case 0xe5: return 0
            case 0xe6: return 0
            case 0xe7: return 0
            case 0xe8: return 0
            case 0xe9: return 0
            case 0xea: return 0
            case 0xeb: return 0
            case 0xec: return 0
            case 0xed: return 0
            case 0xee: return 0
            case 0xef: return 0
            case 0xf0: return 0
            case 0xf1: return 0
            case 0xf2: return 0
            case 0xf3: return 0
            case 0xf4: return 0
            case 0xf5: return 0
            case 0xf6: return 0
            case 0xf7: return 0
            case 0xf8: return 0
            case 0xf9: return 0
            case 0xfa: return 0
            case 0xfb: return 0
            case 0xfc: return 0
            case 0xfd: return 0
            case 0xfe: return 0
            case 0xff: return 0

    opcodes = {
        0x00 : "",
        0x01 : "",
        0x02 : "",
        0x03 : "",
        0x04 : "",
        0x05 : "",
        0x06 : "",
        0x07 : "",
        0x08 : "",
        0x09 : "",
        0x0a : "",
        0x0b : "",
        0x0c : "",
        0x0d : "",
        0x0e : "",
        0x0f : "",
        0x10 : "",
        0x11 : "",
        0x12 : "",
        0x13 : "",
        0x14 : "",
        0x15 : "",
        0x16 : "",
        0x17 : "",
        0x18 : "",
        0x19 : "",
        0x1a : "",
        0x1b : "",
        0x1c : "",
        0x1d : "",
        0x1e : "",
        0x1f : "",
        0x20 : "",
        0x21 : "",
        0x22 : "",
        0x23 : "",
        0x24 : "",
        0x25 : "",
        0x26 : "",
        0x27 : "",
        0x28 : "",
        0x29 : "",
        0x2a : "",
        0x2b : "",
        0x2c : "",
        0x2d : "",
        0x2e : "",
        0x2f : "",
        0x30 : "",
        0x31 : "",
        0x32 : "",
        0x33 : "",
        0x34 : "",
        0x35 : "",
        0x36 : "",
        0x37 : "",
        0x38 : "",
        0x39 : "",
        0x3a : "",
        0x3b : "",
        0x3c : "",
        0x3d : "",
        0x3e : "",
        0x3f : "",
        0x40 : "",
        0x41 : "",
        0x42 : "",
        0x43 : "",
        0x44 : "",
        0x45 : "",
        0x46 : "",
        0x47 : "",
        0x48 : "",
        0x49 : "",
        0x4a : "",
        0x4b : "",
        0x4c : "",
        0x4d : "",
        0x4e : "",
        0x4f : "",
        0x50 : "",
        0x51 : "",
        0x52 : "",
        0x53 : "",
        0x54 : "",
        0x55 : "",
        0x56 : "",
        0x57 : "",
        0x58 : "",
        0x59 : "",
        0x5a : "",
        0x5b : "",
        0x5c : "",
        0x5d : "",
        0x5e : "",
        0x5f : "",
        0x60 : "",
        0x61 : "",
        0x62 : "",
        0x63 : "",
        0x64 : "",
        0x65 : "",
        0x66 : "",
        0x67 : "",
        0x68 : "",
        0x69 : "",
        0x6a : "",
        0x6b : "",
        0x6c : "",
        0x6d : "",
        0x6e : "",
        0x6f : "",
        0x70 : "",
        0x71 : "",
        0x72 : "",
        0x73 : "",
        0x74 : "",
        0x75 : "",
        0x76 : "",
        0x77 : "",
        0x78 : "",
        0x79 : "",
        0x7a : "",
        0x7b : "",
        0x7c : "",
        0x7d : "",
        0x7e : "",
        0x7f : "",
        0x80 : (o.ADD, "B", 1),
        0x81 : "",
        0x82 : "",
        0x83 : "",
        0x84 : "",
        0x85 : "",
        0x86 : (o.ADD, "(HL)", 1),
        0x87 : "",
        0x88 : "",
        0x89 : "",
        0x8a : "",
        0x8b : "",
        0x8c : "",
        0x8d : "",
        0x8e : "",
        0x8f : "",
        0x90 : "",
        0x91 : "",
        0x92 : "",
        0x93 : "",
        0x94 : "",
        0x95 : "",
        0x96 : "",
        0x97 : "",
        0x98 : "",
        0x99 : "",
        0x9a : "",
        0x9b : "",
        0x9c : "",
        0x9d : "",
        0x9e : "",
        0x9f : "",
        0xa0 : "",
        0xa1 : "",
        0xa2 : "",
        0xa3 : "",
        0xa4 : "",
        0xa5 : "",
        0xa6 : "",
        0xa7 : "",
        0xa8 : "",
        0xa9 : "",
        0xaa : "",
        0xab : "",
        0xac : "",
        0xad : "",
        0xae : "",
        0xaf : "",
        0xb0 : "",
        0xb1 : "",
        0xb2 : "",
        0xb3 : "",
        0xb4 : "",
        0xb5 : "",
        0xb6 : "",
        0xb7 : "",
        0xb8 : "",
        0xb9 : "",
        0xba : "",
        0xbb : "",
        0xbc : "",
        0xbd : "",
        0xbe : "",
        0xbf : "",
        0xc0 : "",
        0xc1 : "",
        0xc2 : "",
        0xc3 : "",
        0xc4 : "",
        0xc5 : "",
        0xc6 : (o.ADD, 'I', 2),
        0xc7 : "",
        0xc8 : "",
        0xc9 : "",
        0xca : "",
        0xcb : "",
        0xcc : "",
        0xcd : "",
        0xce : "",
        0xcf : "",
        0xd0 : "",
        0xd1 : "",
        0xd2 : "",
        0xd3 : "",
        0xd4 : "",
        0xd5 : "",
        0xd6 : "",
        0xd7 : "",
        0xd8 : "",
        0xd9 : "",
        0xda : "",
        0xdb : "",
        0xdc : "",
        0xdd : "",
        0xde : "",
        0xdf : "",
        0xe0 : "",
        0xe1 : "",
        0xe2 : "",
        0xe3 : "",
        0xe4 : "",
        0xe5 : "",
        0xe6 : "",
        0xe7 : "",
        0xe8 : "",
        0xe9 : "",
        0xea : "",
        0xeb : "",
        0xec : "",
        0xed : "",
        0xee : "",
        0xef : "",
        0xf0 : "",
        0xf1 : "",
        0xf2 : "",
        0xf3 : "",
        0xf4 : "",
        0xf5 : "",
        0xf6 : "",
        0xf7 : "",
        0xf8 : "",
        0xf9 : "",
        0xfa : "",
        0xfb : "",
        0xfc : "",
        0xfd : "",
        0xfe : "",
        0xff : "",
    }
    # def overflow_check(result, adder):
    #     return adder < result 

    def switch(byte):
        try:
            return o.opcodes[byte]
        except KeyError:
            return "ERROR: UNIMPLEMENTED INSTRUCTION"

    def MOV(dst, src): 
        dst = src

    def NOP():
        pass

    def LXI(byte3, byte2):
        pass

    def STAX():
        pass

    def ADD(x):
        m.A += x 
        m.Carry = m.A < x 
        m.Zero = m.A == 0
        m.Sign = (m.A & 0b1000_0000) > 0
        m.Parity = m.A
        return 1


    def NOP():
        pass

    def NOP():
        pass

    def NOP():
        pass

    def NOP():
        pass

    def NOP():
        pass

    def NOP():
        pass

    def NOP():
        pass

        




    e = 0
    x = lambda : print("NOP"); e+=1

    x()
    a()
    # print("LXI B, D16")

    #0x8_

o = Opcodes