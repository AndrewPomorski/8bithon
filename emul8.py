import sys
from archi import *
from display import displayScreen 
import time
import pygame
import random

TIMER = pygame.USEREVENT + 1

screen = displayScreen(scale_factor=10)
screen.init_display()
'''
############
TODO!!!
Change the way pc is handled, instead of incrementing after the execLoop, it needs to be returned from decoding functions
Right now the GOTO cannot be implemented
#############
'''
def sysinit():    
    # instantiate display and initialize screen
    print("Checking sysinit...")
    #clear memory 
    for i in range(len(memory)):
        #TODO: Don't clear first 512 bits, as they might carry loader data
        memory[i] = 0
    #clear stack 
    for i in range(len(stack)):
        stack[i] = 0    
    stack_p = 0
    global pc
    pc = 512
    global V
    V = [0] * 16
    Index = 0
    global c_flag
    c_flag = ""
    global delay_timer
    delay_timer = 0
    global buzzer_timer
    buzzer_timer = 0
    '''
        Instantiate a TMC1802 CHIP if TMC flag is present in any of first 512 mem addresses.
    '''
    for i in range(0, 512):
        if memory[i] == "TMC":
            print "TMC FOUND"
            #initialize TMC interpreter

    print("Sysinit ok")
    
def loadProgram(fileName):
    print "Loading file: ", fileName
    with open(fileName) as programFile:
        programData = programFile.read().split("\n")

    if len(programData) >= 4096:
        print("Memory error. Aborting.")
        return

    for i in range(len(programData)):
         memory[i + 512] = programData[i]
    
def execLoop():
    # fetch opcode from memory
    # decode opcode with decode_oc() call    
    running = True
    while running:
        while not memory[pc] == "":
            decode_oc(memory[pc])
            global pc
            pc += 1
        pygame.time.wait(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    
    return
    
def decode_oc(opcode):
    #opcode signature - first HEX bit
    ocs = opcode[2]
    if ocs == "0":
        cas_0(opcode)
    elif ocs == "1":
        return "one"
    elif ocs == "2":
        return "two"
    elif ocs == "3":
        return "three"
    elif ocs == "4":
        return "four"
    elif ocs == "5":
        cas_5(opcode)
    elif ocs == "6":
        cas_6(opcode)
    elif ocs == "7":
        cas_7(opcode)
    elif ocs == "8":
        return "eight"
    elif ocs == "9":
        return "nine"
    elif ocs == "A":
        return "ten"
    elif ocs == "B":
        return "eleven"
    elif ocs == "C":
        return "twelve"
    elif ocs == "D":
        cas_D(opcode)
    elif ocs == "E":
        return "fourteen"
    elif ocs == "F":
        return "fifteen"
    else:
        return "Corrupted data. Quiting"
        sys.exit()


################## OPCODES HANDLING################################# 

def cas_0(oc):
    if oc[5] == "0":
        global c_flag
        c_flag = "CLRSC"
        print "CARRY FLAG: ", c_flag
        screen.clear_screen()
        return
    elif oc[5] == "E":
        c_flag  = "RETURN"
        print "CARRY_FLAG: ", c_flag
        '''
            TODO Return from subroutine, allocated only from 0-512 mem addr.
            This routines contain a different instruction set, and will be defined in 1802 Class.
            Those registers might contain binary instructions, encoded in base 16.
            Take care of this later.
        '''
        return 


def cas_5(oc):
    '''
    return
        Simple conditional.
        Skip next instruction if Vx == Vy.
        
        OC: 0x5XY0
        SET:
            0x6001 - V0 = 1
            0x6101 - V1 = 1
            0x5010 - TRUE
        
        Skip next instruction, effectively pc += 2
    '''
    global c_flag
    c_flag = "COND"
    print "CARRY FLAG: ", c_flag
    Xv = oc[3]
    Yv = oc[4]
    X = int(Xv, 16)
    Y = int(Yv, 16)
    if V[X] == V[Y]:
        global pc
        pc += 2
    return


def cas_6(oc):
    '''
        Sets register value to said value
        0x6XNN - set Vx to NN Value
    '''
    global c_flag
    c_flag = "ASGN"
    print "CARRY FLAG: ", c_flag 
    xval = int(oc[3], 16)
    bbval = int(oc[4:6], 16)
    #X = oc[xval]
    #BB = oc[bbval]
    print "oc: ", oc, "X: ", xval, "BB: ", bbval
    global V
    V[xval] = bbval
    print "V RAM: \n", V
    #set Xth register to BB value
    #TODO: decoding of X 


def cas_7(oc):
    '''
        Add function.
        OC: 0x7XNN adds NN to VX
    '''
    global c_flag
    c_flag = "ADDREG"
    print "CARRY FLAG: ", c_flag
    Xv = oc[3]
    X = int(Xv, 16)
    NNv = oc[4:6]
    NN = int(NNv, 16)
    V[X] += NN

def cas_C(oc):
    '''
        Set VX to result of bitwise AND on NN and random number between 0 and 255
        OC: 0xCXNN
    '''
    global c_flag
    c_flag = "RAND"
    print "CARRY FLAG: ", c_flag
    X = int(oc[3], 16)
    NN = int(oc[4:6], 16)
    RN = random.randint(0,255)
    V[X] = X & RN
    
def cas_D(oc):
    #draw instructions
    global c_flag
    c_flag = "DRAW"
    print "CARRY FLAG: ", c_flag
    #TODO set carry_flag to DISP
    oc = oc[2:6]
    print oc
    X = int(oc[1], 16)
    Y = int(oc[2], 16)
    N = int(oc[3], 16)
    VX = V[X]
    VY = V[Y]
    print "X: ", VX, "Y: ", VY
    screen.draw_pixel(VX, VY, 1);
    screen.update()

def cas_F(oc):
    #TODO: two other opcodes end with "5". This needs to be fixed to be more specific
    if oc[5] == "5":
        '''
            OC: 0xFX15
            set the timer to the value of register VX
        '''
        global c_flag
        c_flag = "DELAY"
        print "CARRY FLAG: ", c_flag
        X = int(oc[3], 16)
        global delay_timer
        delay_timer = X
        time.sleep(X)
        return
    elif oc[5] == "7":
        '''
            OC: 0xFX07
            Set the value of the current timer to Vx
        '''
        global c_flag
        c_flag = "SVTIMER"
        print "CARRY FLAG", c_flag
        X = int(oc[3], 16)
        V[X] = delay_timer
        return
    elif oc[5] == "8":
        '''
            OC: OxFX18
            Set the value of sound_timer to VX
        '''
        global c_flag
        c_flag = "SNDTIM"
        print "CARRY FLAG: ", c_flag
        X = int(oc[3], 16)
        global sound_timer
        sound_timer = V[X]
        return


### END OF FILE##############################################
