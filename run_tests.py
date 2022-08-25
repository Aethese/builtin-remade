import os, sys
os.system('cls' if os.name == 'nt' else 'clear')

from rounder import tests as rt
from upper import tests as ut

rounder_test = rt.main()
upper_test = ut.main()

print(f'\n{rounder_test} rounder test(s) failed')
if rounder_test != 0:
	print('Rounder test(s) failed!')
	sys.exit(1)

print(f'\n{upper_test} upper test(s) failed')
if upper_test != 0:
	print('Upper test(s) failed!')
	sys.exit()
