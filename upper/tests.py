import os
from upper import upper
os.system('cls' if os.name == 'nt' else 'clear')

def main():
	'''
	sorry for throwing this so quickly together
	'''
	failed = 0
	print(f'\nRunning Upper version {upper.__version__}')
	original = 'AbCdEakaA'
	new_upper = upper.make_upper(original)
	is_correct = True if new_upper == original.upper() else False
	if not is_correct:
		failed += 1
	print(f'original: {original} | new: {new_upper} | new {"=" if is_correct else "!"}= correct')

	original = 'as8ASd9Af9asdj'
	new_upper = upper.make_upper(original)
	is_correct = True if new_upper == original.upper() else False
	if not is_correct:
		failed += 1
	print(f'original: {original} | new: {new_upper} | new {"=" if is_correct else "!"}= correct')

	return failed
