import os

folder = "/Users/subhashprasad/Downloads/"
for f in os.listdir(folder):
		if f.startswith("u"):	
			print(f)



