import numpy
from memory import Memory as m

class Disassembler:

    used_ops = set()

    def _print_op(actual_op, abstract_op, note = ""):
        d.used_ops.add(abstract_op)
        print(f"{m.PC:04X}  {actual_op:04X}  {note}")

    def print_used_ops():
         print(d.used_ops)
         d.used_ops.clear()

    def disassemble(op1 : numpy.uint8, op2 : numpy.uint8 ):
        op = op1 << 8 | op2
        match op & 0xF000:
            case 0x0000:
                match op & 0xF:
                    # Call opcode (0NNN) not implemented
                    case 0x0: d._print_op(op, "00E0")
                    case 0xE: d._print_op(op, "00EE")

            case 0x1000: d._print_op(op, "1NNN")
            case 0x2000: d._print_op(op, "2NNN")
            case 0x3000: d._print_op(op, "3XNN")
            case 0x4000: d._print_op(op, "4XNN")
            case 0x5000: d._print_op(op, "5XY0")
            case 0x6000: d._print_op(op, "6XNN")
            case 0x7000: d._print_op(op, "7XNN")

            case 0x8000: 
                match op & 0xF:
                    case 0x0: d._print_op(op, "8XY0")
                    case 0x1: d._print_op(op, "8XY1")
                    case 0x2: d._print_op(op, "8XY2")
                    case 0x3: d._print_op(op, "8XY3")
                    case 0x4: d._print_op(op, "8XY4")
                    case 0x5: d._print_op(op, "8XY5")
                    case 0x6: d._print_op(op, "8XY6")
                    case 0x7: d._print_op(op, "8XY7")
                    case 0xE: d._print_op(op, "8XYE")

            case 0x9000: d._print_op(op, "9XY0")
            case 0xA000: d._print_op(op, "ANNN")
            case 0xB000: d._print_op(op, "BNNN")
            case 0xC000: d._print_op(op, "CXNN")
            case 0xD000: d._print_op(op, "DXYN")

            case 0xE000: 
                match op & 0x00FF:
                    case 0x9E: d._print_op(op, "EX9E")
                    case 0xA1: d._print_op(op, "EXA1")

            case 0xF000: 
                match op & 0x00FF:
                    case 0x07: d._print_op(op, "FX07")
                    case 0x0A: d._print_op(op, "FX0A")
                    case 0x15: d._print_op(op, "FX15")
                    case 0x18: d._print_op(op, "FX18")
                    case 0x1E: d._print_op(op, "FX1E")
                    case 0x29: d._print_op(op, "FX29")
                    case 0x33: d._print_op(op, "FX33")
                    case 0x55: d._print_op(op, "FX55")
                    case 0x65: d._print_op(op, "FX65")
            
            case _: print(">>ERROR: UNDEFINED INSTRUCTION<<")

d = Disassembler