from enum import Enum

##INPUT
#8: PC
#9: RAM - ADDRESS
#A: EEPROM - ADDRESS
#B: REG A
#C: REG B
#D: REG I(instruction)
#E: RAM - Write(data)
#F: EEPROM - Write(data)
#
##OUTPUT
#8: PC 	  - OUT
#9: RAM    - OUT
#A: EEPROM - OUT
#B: REG A  - OUT
#C: REG B  - OUT
#D: ALU	  - OUT
#
##ROM 1 (SPECIAL)
#
#01: PC Increment
#02: ALU Carry In
#04: ALU B invert
#08: EEPROM_ARG
#10: JUMP
#20: NC
#40: NC
#80: STEP RESET

# INSTSET BASED ON RAM as Registers
# 0x0 - 0xF
# R0 = 0
# R1 = INST_TMP     # Für Zwischenspeichern von Werten
# R2-R5 = Permanent
# R6-R10 = TEMP
# R11, R12 = Arg
# R13, R14 = Ret
# R15 = SP

class IN(Enum):
    NC      = 0x00
    PC      = 0x80
    RMA     = 0x90
    EPA     = 0xA0
    AR      = 0xB0
    BR      = 0xC0
    IR      = 0xD0
    RM      = 0xE0
    EP      = 0xF0

class OUT(Enum):
    NC      = 0x00
    PC      = 0x08
    RM      = 0x09
    EP      = 0x0A
    AR      = 0x0B
    BR      = 0x0C
    ALU     = 0x0D

class SPEC(Enum):
    PCINC   = 0x01
    ALUCIN  = 0x02
    ALUBINV = 0x04
    EPARG   = 0x08
    JUMP    = 0x10
    DI      = 0x20
    HLT     = 0x40
    RST     = 0x80

class r(Enum):
    z       = 0x0
    s1      = 0x1
    s2      = 0x2
    s3      = 0x3
    s4      = 0x4
    s5      = 0x5
    t1      = 0x6
    t2      = 0x7
    t3      = 0x8
    t4      = 0x9
    t5      = 0xa
    a1      = 0xb
    a2      = 0xc
    r1      = 0xd
    r2      = 0xe
    sp      = 0xf

class c(Enum):
    nop     = 0x0
    add     = 0x1
    sub     = 0x2
    lda     = 0x3
    ldb     = 0x4
    j       = 0x5
    jr      = 0x6
    sr      = 0x7
    lri     = 0x8
    disp    = 0x9
    hlt     = 0xA
    ldai    = 0xB
    ldbi    = 0xC
    sta     = 0xD
    jz      = 0xE


# Umschreiben um C auf Funktionen zu mappen



INST_LEN = 16
RESERVED = 3

instHead = [((OUT.PC, IN.EPA), []),((OUT.EP, IN.IR), [])]
instEnd = [((0,0), [SPEC.PCINC, SPEC.RST])]