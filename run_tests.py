import os, sys
os.system('cls' if os.name == 'nt' else 'clear')

from rounder import tests as rt

rounder_test = rt.main()
if rounder_test != 0:
	print('Rounder test(s) failed!')
	sys.exit(1)
