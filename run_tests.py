import os, sys
os.system('cls' if os.name == 'nt' else 'clear')

from rounder import tests as rt
from upper import tests as ut

rounder_test = rt.main()
upper_test = ut.main()

if rounder_test != 0:
	print('Rounder test(s) failed!')
	sys.exit(1)

if upper_test != 0:
	print('Upper test(s) failed!')
	sys.exit()
