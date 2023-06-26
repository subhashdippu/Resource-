# import glob2,os
# a = glob2.glob(f"/Users/subhashprasad/Movies/*man*")
# if len(a)>1:
#     print("hello")
# else:

# # print(a)
#     for file in glob2.glob(f"/Users/subhashprasad/Movies/*man*"):
#         print(file)
import os
import fnmatch
a = "spider"

folder = "/Users/subhashprasad/Movies/"
for f in os.listdir(folder):
    if os.path.isfile(folder + f):
        if fnmatch.fnmatch(f, f"{a}*"):
            print(f)
            os.system(f'open {folder}/{f}')
            break
            continue
        #     os.system(f"open {a}/{f}")
        elif fnmatch.fnmatch(f, f'{a.capitalize()}*'):
            print(f)
            os.system(f'open {folder}/{f}')
# os.system(f"open {folder}/{a}")