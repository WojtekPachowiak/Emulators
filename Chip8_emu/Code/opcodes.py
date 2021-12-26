import numpy as np 
from memory import Memory as m
from input_output import InputOutput as io

class Opcodes:
    
    def get_bytes(src, mask, rshift):
        # t = type(src)
        # mask = t(mask)
        # rshift = t(rshift)
        a = mask << rshift
        return (src & a) >> rshift

    def combine_bytes(byte1, byte2):
        return byte1 << 8 | byte2        

    # def math_bit_op(a, oper, b):
        # 0b0000_0011 
        # 0x03


    def match_op(op1 , op2 ):
        op = o.combine_bytes(op1, op2)

        

        match op & 0xF000:
            case 0x0000:
                match op & 0xF:
                    # Call opcode (0NNN) not implemented
                    case 0x0: 
                        m.display = np.zeros(m.display.shape, dtype=np.uint8)
                    case 0xE: 
                        m.PC = o.combine_bytes(m.memory[m.SP], m.memory[m.SP+1])
                        m.SP +=2

            case 0x1000: # JUMP
                new_address = o.get_bytes(op,0xFFF,0)
                if new_address == m.PC:
                    print("INFINITE LOOP")
                    m.PC = len(m.rom)
                m.PC = new_address
                
            case 0x2000: 
                m.SP -= 2
                m.memory[m.SP] = o.get_bytes(m.PC+2,0xFF,8) 
                m.memory[m.SP+1] = o.get_bytes(m.PC+2,0xFF,0)
                NNN = o.get_bytes(op,0xFFF,0)
                m.PC = NNN

            case 0x3000: 
                X = o.get_bytes(op,0xF,8)
                NN = o.get_bytes(op,0xFF,0)
                if m.V[X] == NN:
                    m.PC += 2

            case 0x4000: 
                X = o.get_bytes(op,0xF,8)
                NN = o.get_bytes(op,0xFF,0)
                if m.V[X] != NN:
                    m.PC += 2

            case 0x5000: 
                X = o.get_bytes(op,0xF,8)
                Y = o.get_bytes(op,0xF,4)
                if m.V[X] == m.V[Y]:
                    m.PC += 2

            case 0x6000: 
                X = o.get_bytes(op,0xF,8)
                NN = o.get_bytes(op,0xFF,0)
                m.V[X] = NN

            case 0x7000: 
                X = o.get_bytes(op,0xF,8)
                NN = o.get_bytes(op,0xFF,0)
                m.V[X] += NN

            case 0x8000:  # MATH & BINARY MATH
                X = o.get_bytes(op,0xF,8)
                Y = o.get_bytes(op,0xF,4)

                match op & 0xF:
                    case 0x0: 
                        m.V[X] = m.V[Y]
                    case 0x1: 
                        m.V[X] |= m.V[Y]
                    case 0x2: 
                        m.V[X] &= m.V[Y]
                    case 0x3: 
                        m.V[X] ^= m.V[Y]
                    case 0x4: 
                        m.V[X] += m.V[Y]
                        m.V[0xF] = np.uint8(m.V[X] < m.V[Y]) #check overflow
                    case 0x5: 
                        m.V[0xF] = np.uint8(m.V[X] > m.V[Y]) #check borrow
                        m.V[X] -= m.V[Y]
                    case 0x6: 
                        m.V[0xF] = o.get_bytes(m.V[X], 0x1, 0)
                        m.V[X] >>= 1
                    case 0x7: 
                        m.V[0xF] = np.uint8(m.V[Y] > m.V[X]) #check borrow
                        m.V[X] = m.V[Y] - m.V[X]
                    case 0xE: 
                        m.V[0xF] = o.get_bytes(m.V[X], 0x1, 7)
                        m.V[X] <<= m.V[Y]

            case 0x9000: 
                X = o.get_bytes(op,0xF, 8)
                Y = o.get_bytes(op,0xF, 4)
                if m.V[X] != m.V[Y]:
                    m.PC += 2

            case 0xA000: 
                 NNN = o.get_bytes(op,0xFFF, 0)
                 m.I = NNN


            case 0xB000: 
                new_address = o.get_bytes(op,0xFFF,0) + m.V[0]
                if new_address == m.PC:
                    print("INFINITE LOOP")
                    m.PC = len(m.rom) 
                m.PC = new_address

            case 0xC000: 
                X = o.get_bytes(op,0xF, 8)
                NN = o.get_bytes(op,0xFF, 0)
                m.V[X] = np.random.randint(0,255, dtype=np.uint8) & NN

            case 0xD000: 
                X = o.get_bytes(op,0xF, 8)
                Y = o.get_bytes(op,0xF, 4)
                N = o.get_bytes(op,0xF, 0)
            
                arr = np.array(m.memory[m.I:m.I+N]).reshape(N,1)
                sprite = np.unpackbits(arr) 
                
                col = m.V[Y]
                row = m.V[X]
                display_part = m.display[row:row+N, col:col+8]

                m.display[row:row+N, col:col+8] = np.bitwise_xor(display_part, sprite)
                m.V[0xF] = np.any(np.bitwise_and(display_part, sprite))

            case 0xE000: 
                X = o.get_bytes(op,0xF, 8)
                match op & 0x00FF:
                    case 0x9E: 
                        if m.keys[m.V[X]] != 0:
                            m.PC += 2 
                    case 0xA1: 
                        if m.keys[m.V[X]] == 0:
                            m.PC += 2 

            case 0xF000: 
                X = o.get_bytes(op,0xF, 8)
                match op & 0x00FF:
                    case 0x07: 
                        m.V[X] = m.DT
                    case 0x0A: 
                        if not io.waiting_for_input:
                            io.keys_last_frame = io.keys
                            io.waiting_for_input = True
                            m.PC -= 2 
                        else:
                            for i in range(len(io.keys)):
                                if io.keys_last_frame[i] != io.keys[i]:
                                    m.V[X] = i
                                    io.waiting_for_input = False
                                    m.PC += 2 
                            io.keys_last_frame = io.keys
                            m.PC -= 2 

                    case 0x15: 
                        m.DT = m.V[X]
                    case 0x18: 
                        m.ST = m.V[X]
                    case 0x1E: 
                        m.I += m.V[X]
                    case 0x29: 
                        X = o.get_bytes(op,0xF, 8)
                        m.I = m.addr["fonts"] + m.V[X] * 5
                    case 0x33: 
                        v = m.V[X]
                        ones = v % 10
                        v //= 10
                        tens = v % 10
                        hundreds = v // 10
                        m.memory[m.I] = hundreds
                        m.memory[m.I+1] = tens
                        m.memory[m.I+2] = ones
                        # bcd = str()
                        # m.memory[m.I] = np.uint8(bcd[0])
                        # m.memory[m.I+1] = np.uint8(bcd[1])
                        # m.memory[m.I+2] = np.uint8(bcd[2])
                    case 0x55: 
                        # for i in range(X + 1):
                        #     m.memory[m.I+i] = m.V[i]
                        n = len(m.V)
                        m.memory[m.I : m.I+n] = m.V
                        # m.I += X+1 #usedonly in original CHIP8
                    case 0x65: 
                        n = len(m.V)
                        m.V =m.memory[m.I:m.I+n]
                        # m.I += X+1 #usedonly in original CHIP8
            
            case _: print(">>ERROR: UNDEFINED INSTRUCTION<<")

    #{'FX15', '8XY3', '1NNN', '8XY0', '8XY7', 'FX33', 'BNNN', 
    # 'FX55', '8XY5', '4XNN', '8XY2', 'FX1E', 'DXYN', 'EX9E', '3XNN', '8XYE', 'FX65',
    # # 'ANNN', '6XNN', '00E0', '5XY0', 'CXNN', 'FX07', '8XY1', '8XY6', '9XY0', '8XY4', 'FX29', '7XNN'}


o = Opcodes
