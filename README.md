# 8Bit-LogisimEvo
---
-Eigene Adaption von Ben Eaters 8-Bit-PC.

---
# Specs
- 512Byte Program Memory (256 Instruktionen), (256 Argumente)
- 256Byte Random Access Memory - RAM
- 10 Instruktionen
- 2 Register (A und B)

---
# Instruktionen
- 'nop, 0x0   (No Instruction)'
- 'add, addr  (Ram[addr] = A + B)'
- 'sub, addr  (Ram[addr] = A - B)'
- 'lda, addr  (A = Ram[addr])'
- 'ldb, addr  (B = Ram[addr])'
- 'j,   addr  (PC = addr)'
- 'jzr, addr  (if A-B==0, PC = Ram[addr])'
- 'sr,  addr  (Temporary set [Ram address] = addr, to be combined with lri)'
- 'lri, imm   (Ram[Ram address] = imm)'
- 'disp, addr (Displays Ram[addr])'
- 'jz, addr   (if A-B==0, PC = addr)'
