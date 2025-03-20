RAM = [0x00 for _ in range(2^8)]

A = 0x00
B = 0x00

PC = 0x00
RSEL = 0x00
VALUES = 0x00

LOGLEVEL = 0

RUNNING = True

def ins00():
	pass

def ins01():
	global A, B, RSEL
	if RSEL == 0x00:
		A = (A + 0x01) & 0xFF
	else:
		B = (B + 0x01) & 0xFF

def ins02():
	global A, B, RSEL
	if RSEL == 0x00:
		A = (A + B) & 0xFF
	else:
		B = (A + B) & 0xFF

def ins03():
	global RSEL
	if RSEL == 0x00:
		RSEL = 0x01
	else:
		RSEL = 0x00

def ins04():
	global A
	print(chr(A), end="")

def ins05():
	global VALUES
	VALUES = 0x01

def ins06():
	global RUNNING
	RUNNING = False

def ins07():
	global A, B, PC
	PC = (A << 8) | B

def ins08():
	global VALUES
	VALUES = 0x02

def ins09():
	global A, B, RAM
	if RSEL == 0x00:
		RAM[int(B)] = A
	else:
		RAM[int(A)] = B

def ins0A():
	global A, B, RAM
	if RSEL == 0x00:
		A = RAM[int(B)]
	else:
		B = RAM[int(A)]

def process_instruction(instruction):
	if instruction == 0x00: # Pass
		ins00()
	if instruction == 0x01: # Increment selected register
		ins01()
	if instruction == 0x02: # Increment selected register by other register
		ins02()
	if instruction == 0x03: # Switch register
		ins03()
	if instruction == 0x04: # Print
		ins04()
	if instruction == 0x05: # Put next instruction in selected register
		ins05()
	if instruction == 0x06: # End program
		ins06()
	if instruction == 0x07: # Jump to instruction of A and B
		ins07()
	if instruction == 0x08: # Read next 2 instructions into B and A registers
		ins08()
	if instruction == 0x09: # Move selected register to RAM address of non-selected register
		ins09()
	if instruction == 0x0A: # Move RAM address of non-selected register to selected register
		ins0A()

def loop_instructions(instructions):
	global A, B, RSEL, PC, VALUES
	if LOGLEVEL > 3:
		print("DEBUG | VALUES: " + str(VALUES))
		print("DEBUG | PC: " + str(PC))
		print("DEBUG | RAM: " + str(RAM))
		print("DEBUG | A, B: " + str(A) + ", " + str(B))
		input()
	if VALUES == 1:
		A = instructions[PC]
		VALUES -= 1
	elif VALUES == 2:
		B = instructions[PC]
		VALUES -= 1
	else:
		process_instruction(instructions[PC])
	PC += 1

def insloop(instructions):
	while RUNNING:
		loop_instructions(instructions)

