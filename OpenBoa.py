from cpu import MBOA8
from asme import Assembler


running = True

def banner():
    print("OpenBoa 1.0.0, Copyright Mohammed Moustafa Abdelaal, MIT License.")
    print("Independent Kernel CLI for MBOA8 Emulation CPU.")


banner()
asme = Assembler()
program = []
cp = MBOA8(program)
while running:
    command = input("usr@openboa $ ").strip()
    parts = command.split()

    if len(parts) == 0:
        continue

    opcode = parts[0].upper()  # 'ADD', etc.
    if not opcode in asme.valid:
        print(f"{opcode} is not a valid command.")
    else:
        asme.add_code(command + "\nHLT")
        program = asme.parse()
        cp.add_program(program)
        cp.load_program()
        cp.execu()
