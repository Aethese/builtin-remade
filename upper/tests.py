import os
from upper import upper
os.system('cls' if os.name == 'nt' else 'clear')

def main():
	'''
	sorry for throwing this together so quickly
	'''

	failed = 0
	print(f'\nRunning Upper version {upper.__version__}')

	original_string = 'AbCdEakaA'
	new_upper_string = upper.make_upper(original_string)
	is_correct = True if new_upper_string == original_string.upper() else False
	if not is_correct:
		failed += 1
	print(f'original: {original_string} | new: {new_upper_string} | new {"=" if is_correct else "!"}= correct')

	original_string = 'as8ASd9Af9asdj'
	new_upper_string = upper.make_upper(original_string)
	is_correct = True if new_upper_string == original_string.upper() else False
	if not is_correct:
		failed += 1
	print(f'original: {original_string} | new: {new_upper_string} | new {"=" if is_correct else "!"}= correct')

	original_string = 'ALJAkjasd(9139Ajjasd'
	new_lower = upper.make_lower(original_string)
	is_correct = True if new_lower == original_string.lower() else False
	if not is_correct:
		failed += 1
	print(f'original: {original_string} | new: {new_lower} | new {"=" if is_correct else "!"}= correct')

	return failed