import sys

from rounder import tests as rt

rounder_test = rt.main()
if rounder_test != 0:
	print('Rounder test(s) failed!')
	sys.exit(1)
