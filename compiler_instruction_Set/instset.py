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

def Inop():
    i = []
    return i

def I_HLT():
    i = []
    i.append(((OUT.NC,IN.NC),[SPEC.HLT]))
    return i

# Add A and B in Reg[EEP[Arg]]
def IaddABInReg():
    i = []
    i.append(((OUT.EP, IN.RMA), [SPEC.EPARG]))
    i.append(((OUT.ALU, IN.RM), []))
    return i

# Sub B from A in Reg[EEP[Arg]]
def IsubABInReg():
    i = []
    i.append(((OUT.EP, IN.RMA), [SPEC.EPARG]))
    i.append(((OUT.ALU, IN.RM), [SPEC.ALUBINV,SPEC.ALUCIN]))
    return i

# A = Reg[EEP[Arg]]
def IloadA():
    i = []
    i.append(((OUT.EP, IN.RMA), [SPEC.EPARG]))
    i.append(((OUT.RM, IN.AR), []))
    return i

# B = Reg[EEP[Arg]]
def IloadB():
    i = []
    i.append(((OUT.EP, IN.RMA), [SPEC.EPARG]))
    i.append(((OUT.RM, IN.BR), []))
    return i

# Jump to EEP[ARG]
def IJump():
    i = []
    # Must Load zero in A and B
    i.append(((OUT.EP, IN.PC), [SPEC.EPARG]))
    return i

# Jump to EEP[ARG] if Zero
def jumpIfZero():
    i = []
    i.append(((OUT.EP, IN.NC), [SPEC.EPARG, SPEC.JUMP, SPEC.ALUBINV, SPEC.ALUCIN]))
    return i

# Jump befehle Setzen PC auf anderen Wert
# Jump if Alu-Zero to Reg[EEP[Arg]]
def IJumpReg():
    i = []
    i.append(((OUT.EP, IN.RMA), [SPEC.EPARG]))
    i.append(((OUT.RM, IN.NC), [SPEC.JUMP, SPEC.ALUBINV, SPEC.ALUCIN]))
    return i

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

def loadAImm():
    i = []
    i.append(((OUT.EP, IN.AR),[SPEC.EPARG]))
    return i

def loadBImm():
    i = []
    i.append(((OUT.EP, IN.BR),[SPEC.EPARG]))
    return i

def storeAinReg():
    i = []
    i.append(((OUT.EP, IN.RMA),[SPEC.EPARG]))
    i.append(((OUT.AR, IN.RM),[]))
    return i

#              0                 1           2        3         4        5 ...
#            0x0               0x10        0x20     0x30      0x40     0x50 ...
instset = [Inop(), IaddABInReg(), IsubABInReg(), IloadA(), IloadB(), IJump(), IJumpReg(), ISetReg(), ILoadRegImm(), IDispReg(), I_HLT(), loadAImm(), loadBImm(), storeAinReg(), jumpIfZero()] # Muss mit instset_consts.py "c(enum)" übereinstimmen



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

#Use v3 Hex as import

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


