import pygame
from pygame import *
import random
import pygame.surfarray as surfarray
import numpy as np

from Opcodes import Opcodes


WIDTH = 64
HEIGHT = 32
FPS = 60

pygame.init()
pygame.mixer.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chip-8")
CLOCK = pygame.time.Clock()



class Chip8:
    #first 512 for interpreter (0x000-0x200)
    #uppermost 256 for display refresh (0xF00-0xFFF)
    #stack is (0xEA0-0xEFF)
    memory = [0x00] * 4096
    registers = [0x00] * 16
    index = 0x0000
    pc = 0x0000
    stack = [0x0000] * 16
    sp = 0x00
    delayTimer = 0x00
    soundTimer = 0x00
    keypad = [0x00] * 16
    #video = [0x00000000] * WIDTH * HEIGHT
    video = np.zeros((WIDTH, HEIGHT))
    opcode = 0x0000

    
    START_ADRESS = 0x200
    VIDEO_START_ADRESS = 0xF00
    FONTSET_START_ADDRESS = 0x50;

    fontset = [ 0xF0, 0x90, 0x90, 0x90, 0xF0, 
	            0x20, 0x60, 0x20, 0x20, 0x70, 
	            0xF0, 0x10, 0xF0, 0x80, 0xF0, 
	            0xF0, 0x10, 0xF0, 0x10, 0xF0, 
	            0x90, 0x90, 0xF0, 0x10, 0x10, 
	            0xF0, 0x80, 0xF0, 0x10, 0xF0, 
	            0xF0, 0x80, 0xF0, 0x90, 0xF0, 
	            0xF0, 0x10, 0x20, 0x40, 0x40, 
	            0xF0, 0x90, 0xF0, 0x90, 0xF0, 
	            0xF0, 0x90, 0xF0, 0x10, 0xF0, 
	            0xF0, 0x90, 0xF0, 0x90, 0x90, 
	            0xE0, 0x90, 0xE0, 0x90, 0xE0, 
	            0xF0, 0x80, 0x80, 0x80, 0xF0, 
	            0xE0, 0x90, 0x90, 0x90, 0xE0, 
	            0xF0, 0x80, 0xF0, 0x80, 0xF0, 
	            0xF0, 0x80, 0xF0, 0x80, 0x80 ] 
    memory[FONTSET_START_ADDRESS:len(fontset)] = fontset

    opcodes = Opcodes.get_opcodes_dict()
    #for i in range(len(fontset)):
    #    memory[len(fontset) + i] = fontset[i]

    def load_rom(path):
        with open(path, mode = 'rb') as rom:
            #rom = rom.read()
            #print(rom)
            rom = rom.readlines()
            for i in range(len(rom)):
                Chip8.memory[START_ADRESS + i] = rom[i]

    def get_input():
        for i in len(keypad):
            if event.key == pygame.key.key_code(str(hex(i))):
                keypad[i] = 0xFF
        

        #if event.key == pygame.K_0:
        #        keypad[0x0] = 0xFF
        #elif event.key == pygame.K_1:
        #    keypad[0x1] = 0xFF
        #elif event.key == pygame.K_2:
        #    keypad[0x2] = 0xFF
        #elif event.key == pygame.K_3:
        #    keypad[0x3] = 0xFF
        #elif event.key == pygame.K_4:
        #    keypad[0x4] = 0xFF
        #elif event.key == pygame.K_5:
        #    keypad[0x5] = 0xFF
        #elif event.key == pygame.K_6:
        #    keypad[0x6] = 0xFF
        #elif event.key == pygame.K_7:
        #    keypad[0x7] = 0xFF
        #elif event.key == pygame.K_8:
        #    keypad[0x8] = 0xFF
        #elif event.key == pygame.K_9:
        #    keypad[0x9] = 0xFF
        #elif event.key == pygame.K_A:
        #    keypad[0xA] = 0xFF
        #elif event.key == pygame.K_B:
        #    keypad[0xB] = 0xFF
        #elif event.key == pygame.K_C:
        #    keypad[0xC] = 0xFF
        #elif event.key == pygame.K_D:
        #    keypad[0xD] = 0xFF
        #elif event.key == pygame.K_E:
        #    keypad[0xE] = 0xFF
        #elif event.key == pygame.K_F:
        #    keypad[0xF] = 0xFF


    def reset_keypad():
        Chip8.keypad = [0x00 for x in keypad]
    
    def set_timer(sound_timer_val=0, delay_timer_val=0):
        delayTimer = delay_timer_val
        soundTimer = sound_timer_val

    def update_timers():
        if delayTimer > 0:
            delayTimer -= 1
        if soundTimer > 0:
            soundTimer -= 1

    def fetch_op():
        opcode = memory[pc] << 8
        pc += 1
        opcode |= memory[pc]
        pc += 1
        return opcode

    def parse_op(op):
        first_num = (op & 0xF000) > 12
        second_num = (op & 0x0F00) > 8
        third_num = (op & 0x00F0) > 4
        fourth_num = (op & 0x000F)


        if first_num == 0x8:
            opcodes[op_name](second_num, third_num)

        elif first_num == 0x0:
            opcodes[op_name]()

        elif first_num == 0xE or first_num == 0xF:
            opcodes[op_name](second_num)

        #elif first_num in [1,2,0xA,0xB]
        #    if second_num in []
        #    opcodes[op_name](second_num)

    def get_num(val, which_num):
        if type(which_num) == int:
            return (val & which_num) >> (4*which_num)
        elif type(which_num) == list:
            num = 0x0000
            for x in which_num:
                num |= (val >> (4*x)) & 0x000F
            return num


    def execute_op(op_name,):
        opcodes[op_name]()
    
    def update_screen():
        pygame.surfarray.blit_array(SCREEN, video)

    def emu_loop():
        
        opcode = fetch_op()
        execute_op(opcode)
        update_timers()
        update_screen()
        pygame.time.wait(100)


    #def op_0NNN():
    #    nnn = get_num(opcode, [0,1,2])
    #    pc = nnn


    #Clear the screen
    def op_00E0():
        video = np.zeros((WIDTH, HEIGHT),dtype=uint32)
    
    #Returns from a subroutine.
    def op_00EE():
        sp -= 1
        pc = stack[sp]


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

        



        






Chip8.load_rom(r"C:\Users\48501\Desktop\Programming\Python\Chip8_emu\Roms\TETRIS")

running = True
while running:
    CLOCK.tick(FPS)

    Chip8.reset_keypad()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            Chip8.get_input()



    pygame.display.flip()

pygame.quit()
