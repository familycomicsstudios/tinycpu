import tinycpu
import sys
import argparse

tinycpu.LOGLEVEL = 1 # - ERROR WARN LOG DEBUG

def fileToHex(file):
	data = file.read()
	hexList = [byte for byte in data]
	return hexList

def main():
	parser = argparse.ArgumentParser(
		prog='TinyCPU',
		description="A miniature 8-bit CPU written in Python.")
	parser.add_argument('filename')
	parser.add_argument('-l', '--log-level')
	args = parser.parse_args()
	try:
		tinycpu.LOGLEVEL = int(args.log_level)
	except:
		if tinycpu.LOGLEVEL > 0:
			print("ERROR | loglevel must be int")
	if not sys.stdin.isatty():
		file = args.filename
		instructions = fileToHex(sys.stdin.buffer)
	elif len(sys.argv) > 1:
		try:
			with open(args.filename, "rb") as f:
				instructions = fileToHex(f)
		except FileNotFoundError as e:
			if tinycpu.LOGLEVEL > 0:
				print("ERROR | File not found.")
			sys.exit(1)
	else:
		if tinycpu.LOGLEVEL > 0:
			print("ERROR | ROM must be provided with argument or pipe", file=sys.stderr)
		sys.exit(1)
	tinycpu.insloop(instructions)

if __name__ == "__main__":
	main()