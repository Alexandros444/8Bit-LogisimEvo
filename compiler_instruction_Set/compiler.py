from instset_consts import *

# setup = {
#     (c.ldai, 0x0),
#     (c.sta, r.z),
#     (c.sr, r.s1),
#     (c.lri, 0x1),
# }

fib = [
    (c.sr, r.z),
    (c.lri, 0x0),
    # Set Ram Adress Reg to EEP[s1]
    (c.sr, r.s1),   #0
    # Write Ram[EEP[s1]] <= 0
    (c.lri, 0x0),   #1

    (c.sr, r.s2),   #2
    (c.lri, 0x1),   #3
    (c.lda, r.s1),  #4
    (c.ldb, r.s2),  #5
    (c.nop, 0x0),   #6
    (c.add, r.s1),  #7
    (c.lda, r.s1),  #8
    (c.disp, r.s1), #9
    (c.add, r.s2),  #a
    (c.ldb, r.s2),  #b
    (c.disp, r.s2), #c
    
    (c.ldai, 0x0),
    (c.ldbi, 0x0),
    (c.jz, 0x6),     #d
]

test = [
    
    # s1 <= 0
    (c.sr, r.z),   #0
    (c.lri, 0x0),   #1

    # s1 <= 1
    (c.sr, r.s1),   #2
    (c.lri, 0x1),   #3

    # s2 <= 255
    (c.sr, r.s2),   #4
    (c.lri, 0xFF),   #5
    (c.disp, r.s2),  #6   

    # s3 <= 5
    (c.sr, r.s3),   #7
    (c.lri, 0x5),   #8

    # s4 <= 3
    (c.sr, r.s4),   #9
    (c.lri, 0x3),   #A

    # Reg[EEP[Arg]] = A - B
    # t1 = s3 A - s4 B
    (c.lda, r.s3),  #B
    (c.ldb, r.s4),  #C
    (c.sub, r.t1),  #D
    (c.disp, r.t1), #E

    # Reg[EEP[Arg]] = A - B
    # t2 = s4 A - s3 B
    (c.lda, r.s4),  #F
    (c.ldb, r.s3),  #10
    (c.sub, r.t2),  #11
    (c.disp, r.t2), #12

]


countTen = [
    
    # s1 <= 1
    (c.sr, r.s1),   #0
    (c.lri, 0x1),   #1
    
    # Count to 10, loop
    (c.nop, 0x0),    #2 Start

    #t3 = 0A
    (c.sr, r.t3),   #3
    (c.lri, 0x0B),   #4

    #t4 = 0
    (c.sr, r.t4),   #5
    (c.lri, 0x0),   #6

    (c.nop, 0x0),    #7 loop

    #disp t4
    (c.disp, r.t4), #8

    # t4 = t4 + 1
    #a = t4
    (c.lda, r.t4),  #9
    #b = s1
    (c.ldb, r.s1),  #A
    #t4 = a+b
    (c.add, r.t4),  #B

    # if t3 == t4 j start, else loop
    #a = t4
    (c.lda, r.t4),  #C
    #b = t3
    (c.ldb, r.t3),  #D
    # jz :start if t4 == t3
    # (c.jz, 0x2),   #E
    # j loop
    (c.jz, 0x0F),    #E #PC Wird nach Jump noch inkrementiert
    (c.j, 0x7),    #F
    (c.hlt, 0x0)    #10


]

# Version 0.1 EEP_ARG_SPACE = 256
EEP_ARG_SPACE = 1   #Since V0.2

def compile_program(program_code : list[tuple[Enum,Enum|int]]):

    # Fill program Array for adressing with 0
    compiled_code : list[int] = []
    for idx in range(0,2*len(program_code)):
        compiled_code.append(0)

    # Pre define Register Zero for later use

    
    idx = 0
    for instruction in program_code:
        # Instruction IO Hex Code:
        compiled_code[idx] = instruction[0].value

        # Special Instruction Hex Code:
        if isinstance(instruction[1],Enum):
            compiled_code[idx + EEP_ARG_SPACE] = instruction[1].value
        elif isinstance(instruction[1],int):
            compiled_code[idx + EEP_ARG_SPACE] = instruction[1]
        else:
            raise RuntimeError(f"Special Instruction not known Line {idx} {instruction}")
        idx += 2   # V0.2

    lf = 0
    for instruction in compiled_code:
        print ("%0.2X" % instruction, end=" ")
        lf += 1
        if(lf == 16):
            lf = 0
            print()
    return compiled_code


comp_program = countTen

# load zero at start

if __name__ == '__main__':
    compile_program(comp_program)


