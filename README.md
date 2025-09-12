# MBOA8 / MLBOA8 – Mini Boa 8-Bit CPU Emulator

**Tiny. Simple. Educational. Python-powered. Micro\:bit Ready.**

MBOA8 (or MLBOA8) is a **super lightweight 8-bit CPU simulator** written in Python. Designed to **learn CPU basics and opcode execution** in a minimal, approachable way. Perfect for Python experiments or Micro\:bit testing.

---

## ⚡ Features

* **8-bit CPU** with 8 registers (`A`–`H`)
* **256 bytes of memory**
* **Minimal instruction set**:

  * `0x00` – NOP / Padding
  * `0x01` – `LDA` – Load a value from the next memory cell into the accumulator (`A`)
  * `0x02` – `STA` – Store accumulator (`A`) into the next memory cell
  * `0x03` – `ADR` – Add the value from the next memory cell to accumulator (`A`)
  * `0xFF` – `HLT` – Halt execution
* **Custom exception handling** for invalid opcodes
* Tracks **execution time**

---

## 🛠️ Requirements

* Python 3.x (or MicroPython)
* `time` module for execution timing (optional; remove on Micro\:bit)

---

## 💻 How to Use

1. **Write your program as a list of opcodes** (no addresses required, this will be changed in the upgraded GP8BE soon):

```python
program = [
    0x00,  # NOP / padding
    0x01,  # LDA (loads next memory cell into accumulator)
    0x03,  # ADR (adds next memory cell to accumulator)
    0x02,  # STA (stores accumulator to next memory cell)
    0x03,  # ADR again
    0x00,  # NOP
    0xFF   # HLT
]
```

2. **Create a CPU instance, load, and execute**:

```python
cpu = MBOA8(program)
cpu.load_program()
cpu.execu()
```

3. **Check results**:

```python
print("Registers:", cpu.registers)
print("Memory (first 20 cells):", cpu.memory[:20])
```

---

## 🚀 Notes

* The **accumulator (`A`)** is always `registers[0]`.
* The CPU currently **supports only 256 bytes of memory**.
* Your program can run **without pre-filled memory**; the CPU will read and write values as needed.
* Perfect for **learning assembly-style thinking, memory manipulation, and CPU flow**.

---

## 💡 Inspiration

Designed to teach CPU basics, experiment with opcode logic, and test limits on **Micro\:bit or Python**. Minimalistic, lightweight, and fun for hobbyists, students, and curious coders.

---

## 📝 License

MIT / Public Domain – hack, tweak, and experiment freely.
