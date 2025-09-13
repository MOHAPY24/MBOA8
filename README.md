# MLBOA8 – Mini 8-bit Python CPU Emulator

**MLBOA8 (Mini Boa 8-bit)** is a **tiny, educational 8-bit CPU emulator** written in pure Python. Designed for learning, experimentation, and microcontrollers like the **micro\:bit**, MLBOA8 simulates a simple CPU with basic registers, memory, and opcodes — all in under 300 lines of Python code. Perfect for aspiring CPU architects, hobbyists, and coders who want to **build a CPU in Python from scratch**.

---

## Features

* **8-bit architecture** with 8 general-purpose registers (A–H).

* **256-byte memory** for programs and data.

* **Basic instruction set**:

  * `LDA addr` – Load memory into accumulator A
  * `STA addr` – Store accumulator into memory
  * `ADD addr` – Add memory value to accumulator
  * `SUB addr` – Subtract memory value from accumulator
  * `INC reg` / `DEC reg` – Increment/Decrement a register
  * `JMP addr` – Jump to address
  * `JZ addr` / `JNZ addr` – Conditional jumps
  * `SAVE_INTO_B` / `LOAD_FROM_B` – Temp storage using register B
  * `IN addr` / `OUT addr` – Input and output operations
  * `HLT` – Stop program execution

* **Program counter safety** – prevents memory overflow.

* **8-bit arithmetic** – wraps around at 256.

* **Time measurement** – tracks execution time in milliseconds.

---

## Installation

No installation required — MLBOA8 is **pure Python**.

Simply clone the repo or copy the `MLBOA8.py` file into your project. Works on **MicroPython** or standard Python 3.x.

```bash
git clone https://github.com/MOHAPY24/MBOA8.git
cd MBOA8
python3 cpu.py
```

---

## Usage

```python
from MBOA8 import MBOA8

# Sample program
program = [
    0x01, 0x00,  # LDA 0x00
    0x02, 0x01,  # STA 0x01
    0x03, 0x02,  # ADD 0x02
    0xFF         # HLT
]

cpu = MBOA8(program)
cpu.load_program()
cpu.execu()
```

* `program` is a list of **opcodes and operands**.
* `load_program()` maps it into memory.
* `execu()` runs the CPU emulator.

---

## Memory Layout

* 0x00–0xFF: 256-byte memory space.
* Accumulator `A` = register 0, temp register `B` = register 1.
* All arithmetic is **8-bit**, wrapping from 255 → 0.

---

## Development

* Add new **opcodes** by editing the `execu()` method.
* Extend CPU with more registers, I/O, or memory-mapped devices.
* Designed to be **micro\:bit compatible**, just remove `time` imports if using MicroPython.

---

## Contributing

1. Fork the repo
2. Create a branch `feature/new-opcode`
3. Implement your opcode
4. Submit a pull request

---

## License

MIT License – free to use, modify, and teach with.

---

## Example Programs

### Hello World (Pseudo-loop using OUT)

```python
# Print each character from memory until counter = 0
program = [
    0x01, 0x20,  # LDA counter
    0x0E, 0x01,  # SAVE_INTO_B
    # Loop start...
    0x01, 0x10,  # LDA memory[ptr]
    0xDF, 0x10,  # OUT
    0xBF, 0x01,  # DEC counter
    0x0F, 0x03,  # JNZ to Loop start
    0xFF         # HLT
]
```

---

### Notes

* This CPU is **purely educational** — not for production or heavy computation.
* Perfect for **learning how CPUs work**, **assembly logic**, and **emulating minimal architectures**.

