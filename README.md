
# OpenBoa – Mini CPU Emulator (MBOA8)

**Version: 1.0.1**

> CPU learning project using the Von Neumann architecture.
> This release fixes register update errors, cleans code, and improves the opcode parser.

---

## 🔑 Project Intent

OpenBoa is a **mini 8-bit CPU emulator** designed as a **teaching and learning tool**.
It simulates a processor where **code and data share the same memory space**, just like in the Von Neumann model.

The goal is to provide a minimal but functional system that demonstrates:

* How instructions are fetched, decoded, and executed.
* How memory and registers interact.
* How branching, arithmetic, and I/O work at the CPU level.

---

## 🧠 Core Components

### 1. **MBOA8 CPU (cpu.py)**

* **Registers (A–H, 8-bit each):**

  * `A`: Accumulator
  * `B`: Temporary storage
  * `C`: Program counter
  * `D`: Current command
  * `E`: Output
  * `F`: Memory reference
  * `G`, `H`: General-purpose

* **Memory:** 256 bytes (programs + data).

* **Execution cycle:** Fetch → Decode → Execute → Repeat.

* **Safety:** invalid opcodes and memory overflows raise clear errors.

**Supported Instructions:**

* Data: `LDA`, `STA`, `SAVE_INTO_B`, `LOAD_FROM_B`
* Arithmetic: `ADD`, `SUB`, `INC`, `DEC`
* Branching: `JMP`, `JZ`, `JNZ`
* I/O: `INP`, `OUT`, `OUT_MEM`
* Control: `PDI`, `HLT`


Now uses `match, case` instead of long `if, else` chain.

---

### 2. **Assembler (asme.py)**

* Parses human-readable assembly into machine code.
* Accepts hex addresses (e.g., `ADD 0x10`).
* Converts directly into memory images ready to run.

---

### 3. **OpenBoa CLI (OpenBoa.py)**

* REPL-like interactive shell.
* Accepts assembly directly, assembles, loads, and executes it in one step.
* Prints register/memory outputs instantly.

Example:

```bash
usr@openboa $ LDA 0x01
usr@openboa $ ADD 0x02
usr@openboa $ OUT 0x00
usr@openboa $ HLT
```

---

## ⚙️ Features

* **Von Neumann architecture** simulation.
* **Minimal instruction set** for clarity and learning.
* **Assembler pipeline** included—no manual opcodes required.
* **Safe execution** with error handling and bounds checks.
* **Extensible**: easy to add instructions or expand memory.

---

## 🧩 Example Program

```asm
LDA 0x01    ; Load from memory address 0x01
ADD 0x02    ; Add value at address 0x02
OUT 0x00    ; Output accumulator value
HLT         ; Halt execution
```

---

## 📜 Changelog

### v1.0.1

* **Fixed:** `INC (ADC)` and `DEC` registers now properly update values.
* **Removed:** unnecessary/duplicate code for cleaner internals.
* **Improved:** opcode parser migrated from a long `if/else` chain → Python `match/case`.

### v1.0.0

* Initial release of OpenBoa.
* Included CPU, assembler, and CLI shell.

# License
MIT License, do whatever you want.
