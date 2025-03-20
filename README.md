# Tinycpu

A test mini 8-bit CPU.

RAM = 2^8 values

2 registers: A and B

## Commands
### 0x00
Does nothing.
### 0x01
Increment selected register.
### 0x02
Increment selected register by other register.
### 0x03
Switch register. A > B, B > A
### 0x04
Print value of selected register to stdout.
### 0x05
Put next instruction in selected register.
### 0x06
End program.
### 0x07
Jump to selected register's instruction.
### 0x08
Read next 2 instructions into A and B
### 0x09
Move selected register to RAM address of non-selected register
### 0x0A
Move RAM address of non-selected register to selected register
### 0x0B
If A>B, skip next instruction