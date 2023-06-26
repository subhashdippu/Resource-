from pathlib import Path
folder = "/Users/subhashprasad/Movies"
p = Path(folder)
for file in p.glob('**'):
	print(file)
	# print(type(file))
	# print(len(PosixPath))

