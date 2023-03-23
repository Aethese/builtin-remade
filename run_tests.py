import os, sys
os.system('cls' if os.name == 'nt' else 'clear')

from rounder import tests as rt
from upper import tests as ut
from replace import tests as ret

rounder_test = rt.main()
upper_test = ut.main()
replace_test = ret.main()

print(f'\n{rounder_test} rounder test(s) failed')
if rounder_test != 0:
	print('Rounder test(s) failed!')
	sys.exit(1)

print(f'{upper_test} upper test(s) failed')
if upper_test != 0:
	print('Upper test(s) failed!')
	sys.exit(1)

print(f'{replace_test} replace test(s) failed')
if replace_test != 0:
	print('Replace test(s) failed!')
	sys.exit(1)