from instset_consts import *

# # Registeroperationen
# # Base
# def IaddABinA():
#     i = []
#     i.append(((OUT.ALU, IN.AR), []))
#     return i

# def IsubABinA():
#     i = []
#     i.append(((OUT.ALU, IN.AR), [SPEC.ALUBINV,SPEC.ALUCIN]))
#     return i

# # Ramoperationen
# # Write
# def IsaveAinRamB():
#     i = []
#     i.append(((OUT.BR, IN.RMA),[]))
#     i.append(((OUT.AR, IN.RM), []))
#     return i

# def IsaveBinRamA():
#     i = []
#     i.append(((OUT.AR, IN.RMA),[]))
#     i.append(((OUT.BR, IN.RM), []))
#     return i
# # Read
# def IloadAFromRamB():
#     i = []
#     i.append(((OUT.BR, IN.RMA),[]))
#     i.append(((OUT.RM, IN.AR), []))
#     return i

# def IloadBFromRamA():
#     i = []
#     i.append(((OUT.AR, IN.RMA),[]))
#     i.append(((OUT.RM, IN.BR), []))
#     return i

# # EEP Operationen
# # Load Immediate EEP
# def IloadEEPImmidiateInA():
#     i = []
#     i.append(((OUT.PC, IN.EPA), []))
#     i.append(((OUT.EP, IN.AR), [SPEC.EPARG]))
#     return i

# #              0            1             2               3                 4                5                   6
# instset = [IaddABinA(), IsubABinA(),IsaveAinRamB(), IsaveBinRamA(), IloadAFromRamB(),IloadBFromRamA(),IloadEEPImmidiateInA()]



# DESIGN CHANGE '> NO direct REG A AND REG B.
#                   A an B only by Alu with add command and other Register == 0


def Inop():
    i = []
    return i

# Add A and B in Reg[EPARG[PC]]
def IaddABInReg():
    i = []
    # RMA = EPARG[PC]
    i.append(((OUT.EP, IN.RMA), [SPEC.EPARG]))
    # RM[RMA] = ALU (A + B)
    i.append(((OUT.ALU, IN.RM), []))
    return i

# Sub B from A in Reg[EPARG[PC]]
def IsubABInReg():
    i = []
    # RMA = EPARG[PC]
    i.append(((OUT.EP, IN.RMA), [SPEC.EPARG]))
    # RM[RMA] = ALU (A + B)
    i.append(((OUT.ALU, IN.RM), [SPEC.ALUBINV,SPEC.ALUCIN]))
    return i

# A = Reg[EPARG[PC]]
def IloadA():
    i = []
    # RMA = EPARG[PC]
    i.append(((OUT.EP, IN.RMA), [SPEC.EPARG]))
    # A = RM[RMA]
    i.append(((OUT.RM, IN.AR), []))
    return i

# B = Reg[EPARG[PC]]
def IloadB():
    i = []
    # RMA = EPARG[PC]
    i.append(((OUT.EP, IN.RMA), [SPEC.EPARG]))
    # A = RM[RMA]
    i.append(((OUT.RM, IN.BR), []))
    return i

# Jump to EPARG[PC]
def IJump():
    i = []
    # PC = EPARG[PC]
    i.append(((OUT.EP, IN.PC), [SPEC.EPARG]))
    return i

# Jump befehle Setzen PC auf anderen Wert
# Jump if Alu-Zero to Reg[EPARG[PC]]     # Alu is Subtracting
def IJumpZeroReg():
    i = []
    # RMA = EPARG[PC]
    i.append(((OUT.EP, IN.RMA), [SPEC.EPARG]))
    # ALU (A - B) == 0 ? PC = RM[RMA] : PC += 1;
    i.append(((OUT.RM, IN.NC), [SPEC.JUMP,SPEC.ALUBINV,SPEC.ALUCIN]))
    return i


def IJumpZero():
    i = []
    i.append(((OUT.EP, IN.NC), [SPEC.JUMP, SPEC.EPARG, SPEC.ALUBINV, SPEC.ALUCIN]))
    return i

# Set the Adress of the Ram to The Value of the EP-Arg
# RamAddress = EP-Arg
def ISetReg():
    i = []
    i.append(((OUT.EP, IN.RMA), [SPEC.EPARG]))
    return i

def ILoadRegImm():
    i = []
    i.append(((OUT.EP, IN.RM), [SPEC.EPARG]))
    return i

def IDispReg():
    i = []
    i.append(((OUT.EP, IN.RMA), [SPEC.EPARG]))
    i.append(((OUT.RM, IN.NC), [SPEC.DI]))
    return i

#              0                 1           2        3         4        5 ...
#            0x0               0x10        0x20     0x30      0x40     0x50 ...     6           7           8               9           A
instset = [Inop(), IaddABInReg(), IsubABInReg(), IloadA(), IloadB(), IJump(), IJumpZeroReg(), ISetReg(), ILoadRegImm(), IDispReg(), IJumpZero()] # Muss mit instset_consts.py "c(enum)" übereinstimmen

def IHE(inst):
    if(len(inst) > INST_LEN-RESERVED):
        print("ERROR Instruction To Long")
        exit()

    i = []
    for x in instHead:
        i.append(x)
    for x in inst:
        i.append(x)
    for x in instEnd:
        i.append(x)    
    return i


def pInstHex(inst):
    cnt = 0
    for i in inst:
        cnt += 1
        low = 0
        high = 0
        if(i[0][0] != 0):
            low = i[0][0].value
        if(i[0][1] != 0):
            high = i[0][1].value
        print(format(low + high,"02X"),end=' ')
    for i in range(cnt, 16):
        print(format(0,"02X"),end=' ')
    print("")
    cnt = 0
    for i in inst:
        cnt += 1
        sp = 0x00
        for spec in i[1]:
            if(spec == 0):
                continue
            sp += spec.value
        print(format(sp,"02X"),end=' ')
    for i in range(cnt, 16):
        print(format(0,"02X"),end=' ')
    print("")

def pInstIOHex(inst):
    cnt = 0
    for i in inst:
        cnt += 1
        low = 0
        high = 0
        if(i[0][0] != 0):
            low = i[0][0].value
        if(i[0][1] != 0):
            high = i[0][1].value
        print(format(low + high,"02X"),end=' ')
    for i in range(cnt, 16):
        print(format(0,"02X"),end=' ')
    print("")

def pInstSPHex(inst):
    cnt = 0
    for i in inst:
        cnt += 1
        sp = 0x00
        for spec in i[1]:
            if(spec == 0):
                continue
            sp += spec.value
        print(format(sp,"02X"),end=' ')
    for i in range(cnt, 16):
        print(format(0,"02X"),end=' ')
    print("")

import sys

if len(sys.argv) > 1:
    if sys.argv[1] == "io":
        for inst in instset:
            pInstIOHex(IHE(inst))
    elif sys.argv[1] == "spec":
        for inst in instset:
            pInstSPHex(IHE(inst))
else:
    for inst in instset:
        pInstHex(IHE(inst))


