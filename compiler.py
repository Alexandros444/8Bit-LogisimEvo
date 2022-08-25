from instset_consts import *

code = [
    (c.sr, r.s1),   #0
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

pre_comp = []
for i in range(0,512):
    pre_comp.append(0)
line = 0

for i in code:
    pre_comp[line] = i[0].value
    #print("0x%0.2X" % i[0].value, end=" ")
    try:
        pre_comp[line + 256] = i[1].value
     #   print("0x%0.2X" % i[1].value)
    except:
        pre_comp[line + 256] = i[1]
      #  print("0x%0.2X" % i[1])
    line += 1

lf = 0
for i in pre_comp:
    print ("%0.2X" % i, end=" ")
    lf += 1
    if(lf == 16):
        lf = 0
        print()