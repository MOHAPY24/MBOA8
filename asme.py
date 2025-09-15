
import re


class Assembler:
    def __init__(self, code:str=None):
        self.code = code
        self.pointer = 0
        self.current = None
        self.memory = [0] * 256
        self.comment = False
        self.valid = [
            "LDA",
            "STA",
            "PDI",
            "ADD",
            "SAVE_INTO_B",
            "LOAD_FROM_B",
            "SUB",
            "JMP",
            "JZ",
            "JNZ",
            "ADC",
            "DEC",
            "OUT",
            "INP",
            "HLT",
            "OUT_MEM"
        ]


    def add_code(self, codetoadd:str=None):
        self.code = codetoadd



    def parse(self):
        for i in self.code.strip().splitlines():

            if self.comment:
                pass

            if "LDA" in i and not self.comment:
                self.memory[self.pointer] = 0x01
                hex_matches = re.findall(r'0x[0-9A-Fa-f]+', i.replace("LDA", ''))

                hex_list = [int(h, 16) for h in hex_matches]
                self.memory[self.pointer + 1] = int(str(hex_list).replace('[', '').replace(']', ''))
                self.pointer += 1

            if "PDI" in i and not self.comment:
                self.memory[self.pointer] = 0x00

            elif "STA" in i and not self.comment:
                self.memory[self.pointer] = 0x02
                hex_matches = re.findall(r'0x[0-9A-Fa-f]+', i.replace("STA", ''))

                hex_list = [int(h, 16) for h in hex_matches]
                self.memory[self.pointer + 1] = int(str(hex_list).replace('[', '').replace(']', ''))
                self.pointer += 1
            elif "ADD" in i and not self.comment:
                self.memory[self.pointer] = 0x03
                hex_matches = re.findall(r'0x[0-9A-Fa-f]+', i.replace("ADD", ''))

                hex_list = [int(h, 16) for h in hex_matches]
                self.memory[self.pointer + 1] = int(str(hex_list).replace('[', '').replace(']', ''))
                self.pointer += 1

            elif "SAVE_INTO_B" in i and not self.comment:
                self.memory[self.pointer] = 0x0D
                hex_matches = re.findall(r'0x[0-9A-Fa-f]+', i.replace("SAVE_INTO_B", ''))

                hex_list = [int(h, 16) for h in hex_matches]
                self.memory[self.pointer + 1] = int(str(hex_list).replace('[', '').replace(']', ''))
                self.pointer += 1

            elif "LOAD_FROM_B" in i and not self.comment:
                self.memory[self.pointer] = 0x0E
                hex_matches = re.findall(r'0x[0-9A-Fa-f]+', i.replace("LOAD_FROM_B", ''))

                hex_list = [int(h, 16) for h in hex_matches]
                self.memory[self.pointer + 1] = int(str(hex_list).replace('[', '').replace(']', ''))
                self.pointer += 1

            elif "SUB" in i and not self.comment:
                self.memory[self.pointer] = 0x0B
                hex_matches = re.findall(r'0x[0-9A-Fa-f]+', i.replace("SUB", ''))

                hex_list = [int(h, 16) for h in hex_matches]
                self.memory[self.pointer + 1] = int(str(hex_list).replace('[', '').replace(']', ''))
                self.pointer += 1

            elif "JMP" in i and not self.comment:
                self.memory[self.pointer] = 0x0A
                hex_matches = re.findall(r'0x[0-9A-Fa-f]+', i.replace("JMP", ''))

                hex_list = [int(h, 16) for h in hex_matches]
                self.memory[self.pointer + 1] = int(str(hex_list).replace('[', '').replace(']', ''))
                self.pointer += 1

            elif "JNZ" in i and not self.comment:
                self.memory[self.pointer] = 0x0F
                hex_matches = re.findall(r'0x[0-9A-Fa-f]+', i.replace("JNZ", ''))

                hex_list = [int(h, 16) for h in hex_matches]
                self.memory[self.pointer + 1] = int(str(hex_list).replace('[', '').replace(']', ''))
                self.pointer += 1

            elif "ADC" in i and not self.comment:
                self.memory[self.pointer] = 0xAF
                hex_matches = re.findall(r'0x[0-9A-Fa-f]+', i.replace("ADC", ''))

                hex_list = [int(h, 16) for h in hex_matches]
                self.memory[self.pointer + 1] = int(str(hex_list).replace('[', '').replace(']', ''))
                self.pointer += 1

            elif "DEC" in i and not self.comment:
                self.memory[self.pointer] = 0xBF
                hex_matches = re.findall(r'0x[0-9A-Fa-f]+', i.replace("DEC", ''))

                hex_list = [int(h, 16) for h in hex_matches]
                self.memory[self.pointer + 1] = int(str(hex_list).replace('[', '').replace(']', ''))
                self.pointer += 1

            elif "INP" in i and not self.comment:
                self.memory[self.pointer] = 0xCF
                hex_matches = re.findall(r'0x[0-9A-Fa-f]+', i.replace("IN", ''))

                hex_list = [int(h, 16) for h in hex_matches]
                self.memory[self.pointer + 1] = int(str(hex_list).replace('[', '').replace(']', ''))
                self.pointer += 1

            elif "OUT" in i and not self.comment:
                self.memory[self.pointer] = 0xDF
                hex_matches = re.findall(r'0x[0-9A-Fa-f]+', i.replace("OUT", ''))

                hex_list = [int(h, 16) for h in hex_matches]
                self.memory[self.pointer + 1] = int(str(hex_list).replace('[', '').replace(']', ''))
                self.pointer += 1

            elif "OUT_MEM" in i and not self.comment:
                self.memory[self.pointer] = 0xEF
                hex_matches = re.findall(r'0x[0-9A-Fa-f]+', i.replace("OUT_MEM", ''))

                hex_list = [int(h, 16) for h in hex_matches]
                self.memory[self.pointer + 1] = int(str(hex_list).replace('[', '').replace(']', ''))
                self.pointer += 1

            elif '\t' in i or '\n' in i or ' ' in i:
                pass

            elif "HLT" in i and not self.comment:
                self.memory[self.pointer] = 0xFF

            self.pointer += 1

        return self.memory


