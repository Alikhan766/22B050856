import os
print('Exist:', os.access('c:\\Users\\Public\\test.txt', os.F_OK))
print('Readable:', os.access('c:\\Users\\Public\\test.txt', os.R_OK))
print('Writable:', os.access('c:\\Users\\Public\\test.txt', os.W_OK))
print('Executable:', os.access('c:\\Users\\Public\\test.txt', os.X_OK))
