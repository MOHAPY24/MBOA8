# MBOA8/MLBOA8 is ment to simpily simulate a very very very simple 8-bit CPU for learning and integration
# PS: I made this to be used on a microbit to test its limits.



import time # remove if using micropython/microbit

class InvalidOpcode(Exception):
    def __init__(self, code, addr):
        Exception(f'Opcode {code} at address {addr} is not a valid opcode.')

class MBOA8: # Mini Boa (Python Based) 8 bit
    def __init__(self, program:list):
        self.program = program
        self.memory = [0] * 256
        self.registers = [0] * 8
        self.pc = 0
        self.opcode = 0x00
        self.clock_strt = time.time()
    
    def load_program(self, start_addr:int=0x00): # Map the memory
        for i, byte in enumerate(self.program):
            self.memory[start_addr + i] = byte
        return start_addr

    def add_program(self, programs:list=None):
        self.program = programs


    def step(self, speed:int=0):
        time.sleep(speed)
        save_Code = self.program
        self.program = self.program[self.pc]
        self.program[self.pc + 1] = 0xFF
        self.load_program(self.pc)
        self.execu()
        self.program = save_Code


    
    def execu(self): # Execute the opcodes
        halted = False # 0xFF
        a = self.registers[0] # A (register 0) is now an accumulator
        b = self.registers[1] # B (register 1) is now temp memory
        c = self.registers[2] # C (register 2) is now program pointer
        d = self.registers[3] # D (register 3) is now current command
        e = self.registers[4] # E (register 4) is now the current output
        f = self.registers[5] # F (register 5) is now the current memory
        g = self.registers[6]
        h = self.registers[7]
        
        while not halted:
            self.opcode = self.memory[self.pc] # Grab opcode
            f = self.memory
            d = self.opcode
            self.pc += 1
            c = self.pc
            
            
            if self.pc > 255:
                raise IndexError("Program counter over 256 hexadecimal limit.")

            match self.opcode:
                case 0x00:
                    time.sleep(0.05)
                    continue
                case 0x01: # LDA
                    addr = self.memory[self.pc] & 0xFF
                    self.pc += 1
                    a = self.memory[addr]
                case 0x02: # STA
                    addr = self.memory[self.pc] & 0xFF
                    self.pc += 1
                    self.memory[addr] = a
                case 0x03: # ADD
                    addr = self.memory[self.pc] & 0xFF
                    print(addr)
                    self.pc += 1
                    a =  (a + self.memory[addr]) & 0xFF
                case 0x0D: # SAVE_INTO_B
                    addr = self.memory[self.pc] & 0xFF
                    self.pc += 1
                    b = self.memory[addr]
                case 0x0E: # LOAD_FROM_B
                    addr = self.memory[self.pc] & 0xFF
                    self.pc += 1
                    self.memory[addr] = (self.memory[addr] + b) & 0xFF
                    b = 0 # Clear temp
                case 0x0B: # SUB
                        addr = self.memory[self.pc] & 0xFF
                        self.pc += 1
                        a = (a - self.memory[addr]) & 0xFF
                case 0x0A: # JMP
                    addr = self.memory[self.pc] & 0xFF
                    self.pc = addr
                case 0x0C: # JZ
                    addr = self.memory[self.pc] & 0xFF
                    if a == 0:
                        self.pc = addr
                case 0x0F: # JNZ
                    addr = self.memory[self.pc] & 0xFF
                    if a != 0:
                        self.pc = addr
                case 0xAF: # INC
                    reg_addr = self.memory[self.pc] & 0x07
                    self.pc += 1
                    if reg_addr == 0x05:
                        raise IndexError("Trying to manipulate Register F (array) with an int method.")
                    self.registers[reg_addr] += 1 & 0xFF
                    a = self.registers[0]  # A (register 0) is now an accumulator
                    b = self.registers[1]  # B (register 1) is now temp memory
                    c = self.registers[2]  # C (register 2) is now program pointer
                    d = self.registers[3]  # D (register 3) is now current command
                    e = self.registers[4]  # E (register 4) is now the current output
                    f = self.registers[5]  # F (register 5) is now the current memory
                    g = self.registers[6]
                    h = self.registers[7]
                case 0xBF: # DEC
                    reg_addr = self.memory[self.pc] & 0x07
                    self.pc += 1
                    if reg_addr == 0x05:
                        raise IndexError("Trying to manipulate Register F (array) with an int method.")
                    self.registers[reg_addr] -= 1 & 0xFF
                    a = self.registers[0]  # A (register 0) is now an accumulator
                    b = self.registers[1]  # B (register 1) is now temp memory
                    c = self.registers[2]  # C (register 2) is now program pointer
                    d = self.registers[3]  # D (register 3) is now current command
                    e = self.registers[4]  # E (register 4) is now the current output
                    f = self.registers[5]  # F (register 5) is now the current memory
                    g = self.registers[6]
                    h = self.registers[7]
                case 0xCF: # INP
                    addr = self.memory[self.pc] & 0xFF
                    self.pc += 1
                    try:
                        a += int(input("")) & 0xFF
                    except ValueError:
                        raise ValueError("Cannot take in non int value.")
                case 0xDF: # OUT

                    reg_addr = self.memory[self.pc] & 0x07

                    self.pc += 1
                    match reg_addr:
                        case 0x00:
                            e = a
                            print(a)
                        case 0x01:
                            e = b
                            print(b)
                        case 0x02:
                            e = c
                            print(c)
                        case 0x03:
                            e = d
                            print(d)
                        case 0x04:
                            print(e)
                        case 0x05:
                            e = f
                            print(f)
                        case 0x06:
                            e = g
                            print(g)
                        case 0x07:
                            e = h
                            print(h)
                        case _:
                            raise InvalidOpcode(self.opcode, reg_addr)

                case 0xEF:  # OUT_MEM
                    addr = self.memory[self.pc] & 0xFF

                    self.pc += 1
                    print(self.memory[addr])
                        
                case 0xFF: # HLT
                    halted = True
            
            
                case _:
                    raise InvalidOpcode(self.opcode, self.memory[self.pc-1])

            self.registers[0] = a & 0xFF
            self.registers[1] = b & 0xFF
            self.registers[2] = c & 0xFF
            self.registers[3] = d & 0xFF
            self.registers[4] = e
            self.registers[5] = f & 0xFF
            self.registers[6] = g & 0xFF
            self.registers[7] = h & 0xFF

            self.clock_end = time.time()
            self.elapsed = (self.clock_end - self.clock_strt) * 10000
            #print(f"Time Elapsed: {self.elapsed:.2f} ms")
            
