from instset_consts import *

fib = [
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
    (c.j, 0x6),     #d
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
    (c.lri, 0x0A),   #4

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
    (c.jz, 0x2),   #E
    # j loop
    (c.j, 0x7),    #F


]




pre_comp = []
for i in range(0,512):
    pre_comp.append(0)
line = 0


# Version 0.1 EEP_ARG_SPACE = 256
EEP_ARG_SPACE = 1   #Since V0.2


for i in fib:
    pre_comp[line] = i[0].value
    #print("0x%0.2X" % i[0].value, end=" ")
    try:
        pre_comp[line + EEP_ARG_SPACE] = i[1].value
     #   print("0x%0.2X" % i[1].value)
    except:
        pre_comp[line + EEP_ARG_SPACE] = i[1]
      #  print("0x%0.2X" % i[1])
    line += 2   # V0.2

lf = 0
for i in pre_comp:
    print ("%0.2X" % i, end=" ")
    lf += 1
    if(lf == 16):
        lf = 0
        print()