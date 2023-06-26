import fnmatch
import os
# a = "man"
# folder = "/Users/subhashprasad/Movies/"
# c = f'{a}*' or f'{a.capitalize()}*' or f'*{a.upper()}' or f'*{a}*' or f'*{a.capitalize()}*' or f'*{a.upper()}' or f'*{a}' or f'*{a.capitalize()}' or f'*{a.upper()}'
# for f in os.listdir(folder):
# 	if os.path.isfile(folder + f): # This will print only file not folder
# 		# if fnmatch.fnmatch(f, '*Regression*'): # first argument is filename, second argument is search file (*) means something
# 		if fnmatch.fnmatch(f, c): # starts with A and something in between and ends with .py
# 			print(f)

b = "/Users/subhashprasad/Movies/"  # without this program not going to run
for f in os.listdir(b):
    if os.path.isfile(b + f):
        # if fnmatch.fnmatch(f, f'{a}*' or f'{a.capitalize()}*' or f'*{a.upper()}' or f'*{a}*' or f'*{a.capitalize()}*' or f'*{a.upper()}' or f'*{a}' or f'*{a.capitalize()}' or f'*{a.upper()}'):
        #     # print(f)
        #     os.system(f"open {b}/{f}")
        # 	if fnmatch.fnmatch(f, '*Regression*'): # first argument is filename, second argument is search file (*) means something
        if fnmatch.fnmatch(f, 'Jai*'):
            print(f)
