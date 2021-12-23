from memory import Memory

_m = Memory

class Opcodes:
    
    opcodes_dict = {
        0x00E0 : _m.op_00E0,
        0x00E0 : _m.op_00E0,
        0x00E0 : _m.op_00E0,
        0x00E0 : _m.op_00E0,
        0x00E0 : _m.op_00E0,
        0x00E0 : _m.op_00E0,
    }

    #Clear the screen
    def op_00E0():
        video = np.zeros((WIDTH, HEIGHT),dtype=uint32)
    
    #Returns from a subroutine.
    def op_00EE():
        m.SP -= 1
        m.PC = stack[m.SP]


    #Returns from a subroutine.
    def op_1NNN():
        nnn = get_num(opcode, [0,1,2])
        pc = nnn

    #Calls subroutine at NNN.
    def op_2NNN():
        stack[sp] = pc
        stack +=1
        pc = get_num(opcode, [0,1,2])

    #Skips the next instruction if VX equals NN. (Usually the next instruction is a jump to skip a code block);
    def op_3XNN():
        x = get_num(opcode, 2)
        nn = get_num(opcode, [0,1])
        if registers[x] == nn:
            pc +=2

    #Skips the next instruction if VX does not equal NN. (Usually the next instruction is a jump to skip a code block);
    def op_4XNN():
        x = get_num(opcode, 2)
        nn = get_num(opcode, [0,1])
        if registers[x] != nn:
            pc +=2

    #Skips the next instruction if VX equals VY. (Usually the next instruction is a jump to skip a code block);
    def op_5XY0():
        x = get_num(opcode, 2)
        y = get_num(opcode, 1)
        if registers[x] == registers[y]:
            pc +=2

    #Sets VX to NN.
    def op_6XNN():
        x = get_num(opcode, 2)
        nn = get_num(opcode, [0,1])
        registers[x] = nn

    #Adds NN to VX. (Carry flag is not changed);
    def op_7XNN():
        x = get_num(opcode, 2)
        nn = get_num(opcode, [0,1])
        registers[x] += vx

    def op_1NNN():
        nnn = get_num(opcode, [0,1,2])
        pc = nnn

    def op_1NNN():
        nnn = get_num(opcode, [0,1,2])
        pc = nnn

    #Store number NN in register VX
    def op_6XNN():
        x = get_num(opcode,3) 
        nn = get_num(opcode,3) 
        registers[x] = nn
        

    #Store the value of register VY in register VX
    def op_8XY0():
        pass

    #Add the value NN to register VX
    def op_7XNN():
        pass


