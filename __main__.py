import tinycpu
import sys

tinycpu.LOGLEVEL = 1 # - ERROR WARN LOG DEBUG

def fileToHex(file):
	data = file.read()
	hexList = [byte for byte in data]
	return hexList

def main():
	if not sys.stdin.isatty():
		file = sys.argv[1]
		instructions = fileToHex(sys.stdin.buffer)
	elif len(sys.argv) > 1:
		try:
			with open(sys.argv[1], "rb") as f:
				instructions = fileToHex(f)
		except FileNotFoundError as e:
			if LOGLEVEL > 0:
				print("ERROR | File not found.")
			sys.exit(1)
	else:
		if LOGLEVEL > 0:
			print("ERROR | ROM must be provided with argument or pipe", file=sys.stderr)
		sys.exit(1)
	tinycpu.insloop(instructions)

if __name__ == "__main__":
	main()