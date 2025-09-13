# MBOA8/MLBOA8 is ment to simpily simulate a very very very simple 8 bit CPU for learning and integration
# PS: I made this to be used on a microbit to test its limits.



import time # remove if using micropython/microbit

class InvalidOpcode(Exception):
    def __init__(self, code, addr):
        Exception(f'Opcode {code} at address {addr} is not a valid opcode.')

class MBOA8: # Mini Boa (Python Based) 8 bit
    def __init__(self, program:list):
        self.program = program
        self.memory = [0] * 256
        self.registers = [0] * 8 # A (accumelator), B, C, D, E, F, G, H
        self.pc = 0
        self.opcode = 0x00
        self.clock_strt = time.time()
        self.load_program(0x00)
    
    def load_program(self, start_addr:int=0x00): # Map the memory
        for i, byte in enumerate(self.program):
            self.memory[start_addr + i] = byte
        return start_addr
    
    def execu(self): # Execute the opcodes
        halted = False # 0xFF
        a = self.registers[0] # A (register 0) is now an accumelator
        b = self.registers[1] # B (register 1) is now temp memory
        
        while not halted:
            self.opcode = self.memory[self.pc] # Grab opcode
            self.pc += 1
            
            
            if self.pc > 255:
                raise IndexError("Program counter over 256 hexidecimal limit.")
            
            print(self.opcode)
                   
            if self.opcode == 0x00: # Padding
                continue
            elif self.opcode == 0x01: # LDA
                addr = self.memory[self.pc] & 0xFF
                self.pc += 1
                a = self.memory[addr]
            elif self.opcode == 0x02: # STA
                addr = self.memory[self.pc] & 0xFF
                self.pc += 1
                self.memory[addr] = a
            elif self.opcode == 0x03: # ADD
                addr = self.memory[self.pc] & 0xFF
                print(addr)
                self.pc += 1
                a =  (a + self.memory[addr]) & 0xFF
            elif self.opcode == 0x0D: # SAVE_INTO_B
                addr = self.memory[self.pc] & 0xFF
                self.pc += 1
                b = self.memory[addr] 
            elif self.opcode == 0x0E: # LOAD_FROM_B
                addr = self.memory[self.pc] & 0xFF
                self.pc += 1
                self.memory[addr] = (self.memory[addr] + b) & 0xFF
                b = 0 # Clear temp
            elif self.opcode == 0x0B: # SUB
                addr = self.memory[self.pc] & 0xFF
                self.pc += 1
                a = (a - self.memory[addr]) & 0xFF
            elif self.opcode == 0x0A: # JMP
                addr = self.memory[self.pc] & 0xFF
                self.pc = addr
            elif self.opcode == 0x0C: # JZ
                addr = self.memory[self.pc] & 0xFF
                if a == 0:
                    self.pc = addr
            elif self.opcode == 0x0F: # JNZ
                addr = self.memory[self.pc] & 0xFF
                if a != 0:
                    self.pc = addr
            elif self.opcode == 0xAF: # INC
                reg_addr = self.memory[self.pc] & 0x07
                self.pc += 1
                self.registers[reg_addr] = (self.registers[reg_addr] + 1) & 0xFF
            elif self.opcode == 0xBF: # DEC
                reg_addr = self.memory[self.pc] & 0x07
                self.pc += 1
                self.registers[reg_addr] = (self.registers[reg_addr] - 1) & 0xFF
            elif self.opcode == 0xCF: # IN
                addr = self.memory[self.pc] & 0xFF
                self.pc += 1
                try:
                    self.memory[addr] = int(input("")) & 0xFF 
                except ValueError:
                    raise ValueError("Cannot take in non int value.")
            elif self.opcode == 0xDF: # OUT
                addr = self.memory[self.pc] & 0xFF
                self.pc += 1
                print(self.memory[addr])
                        
            elif self.opcode == 0xFF: # HLT
                halted = True
            
            
            else:
                raise InvalidOpcode(self.opcode, self.memory[self.pc-1])
            
            self.registers[0] = a & 0xFF
            self.registers[1] = b & 0xFF

        self.clock_end = time.time()
        self.elapsed = (self.clock_end - self.clock_strt) * 10000
        print(f"Time Elapsed: {self.elapsed:.2f} ms")
            
if __name__ == "__main__":
    program = [0x01, 0x00, 0x02, 0x00, 0x03, 0x00, 0xFF] # Define opcodes
    cpinst = MBOA8(program) # Define CPU instance
    cpinst.load_program()
    cpinst.execu() # Execute
