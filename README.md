
# OpenBoa

**OpenBoa** is a Python-based emulator for the **MBOA8** CPU (Mini Boa 8-bit).
It includes a CPU emulator, an assembler, and an interactive kernel so you can test assembly instructions in real time.

This project is designed as an educational playground to show how instructions, memory, and registers all work together at the most basic level of computer architecture.

---

## CPU Overview

* **Memory:** 256 bytes (0x00–0xFF)

* **Registers:** 8 total →

  * `0x00` → A (accumulator)
  * `0x01` → B (temp memory)
  * `0x02` → C
  * `0x03` → D
  * `0x04` → E
  * `0x05` → F
  * `0x06` → G
  * `0x07` → H

* **PC (Program Counter):** tracks the next instruction address

* **Execution Model:** Fetch → Decode → Execute loop

* **Instruction Size:** 2 bytes → (opcode + operand), except `PDI` and `HLT` which are single byte

---

## Instruction Set

| Mnemonic           | Opcode | Operand Type              | Description                                |
| ------------------ | ------ | ------------------------- | ------------------------------------------ |
| `PDI`              | `0x00` | none                      | Padding/NOP (does nothing, one cycle)      |
| `LDA addr`         | `0x01` | memory addr (0x00–0xFF)   | Load memory\[addr] into A                  |
| `STA addr`         | `0x02` | memory addr               | Store A into memory\[addr]                 |
| `ADD addr`         | `0x03` | memory addr               | Add memory\[addr] to A                     |
| `SUB addr`         | `0x0B` | memory addr               | Subtract memory\[addr] from A              |
| `JMP addr`         | `0x0A` | memory addr               | Jump unconditionally to addr               |
| `JZ addr`          | `0x0C` | memory addr               | Jump to addr if A == 0                     |
| `JNZ addr`         | `0x0F` | memory addr               | Jump to addr if A != 0                     |
| `SAVE_INTO_B addr` | `0x0D` | memory addr               | Copy memory\[addr] into register B         |
| `LOAD_FROM_B addr` | `0x0E` | memory addr               | Add B into memory\[addr], then clear B     |
| `ADC reg_addr`     | `0xAF` | register addr (0x00–0x07) | Increment register\[reg\_addr] by 1        |
| `DEC reg_addr`     | `0xBF` | register addr             | Decrement register\[reg\_addr] by 1        |
| `INP addr`         | `0xCF` | memory addr               | Take integer input, place in memory\[addr] |
| `OUT reg_addr`     | `0xDF` | register addr             | Print contents of register\[reg\_addr]     |
| `OUT_MEM addr`     | `0xEF` | memory addr               | Print contents of memory\[addr]            |
| `HLT`              | `0xFF` | none                      | Halt execution                             |

**Key Rules:**

* All instructions require operands except `PDI` and `HLT`.
* Register operands must be between `0x00` and `0x07`.
* Memory operands must be between `0x00` and `0xFF`.

---

## Usage

### Run the Kernel

```bash
python OpenBoa.py
```

Banner shows:

```
OpenBoa 1.0.0, Copyright Mohammed Moustafa Abdelaal, GPL-3.0 License.
Independent Kernel CLI for MBOA8 Emulation CPU.
```

Now type instructions directly.

---

## Example Programs

### 1. Print the Accumulator

```
usr@openboa $ LDA 0x05
usr@openboa $ OUT 0x00
```

* Loads memory\[0x05] into A.
* Prints A (register 0x00).

---

### 2. Increment Register H

```
usr@openboa $ ADC 0x07
usr@openboa $ OUT 0x07
```

* Increments H by 1.
* Prints H.

---

### 3. Input and Store

```
usr@openboa $ INP 0x10
usr@openboa $ LDA 0x10
usr@openboa $ OUT 0x00
```

* Reads integer input, stores in memory\[0x10].
* Loads it into A.
* Prints A.

---

### 4. Branching Example

```
usr@openboa $ LDA 0x20
usr@openboa $ SUB 0x21
usr@openboa $ JZ 0x30
usr@openboa $ OUT 0x00
```

* Compares memory\[0x20] with memory\[0x21].
* If equal → jumps to address 0x30.
* Else → prints accumulator A.

---

## License

GPL-3.0 License
