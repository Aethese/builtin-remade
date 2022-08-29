from replace import replace

def main():
	failed = 0
	print(f'\nRunning Replace version {replace.__version__}')

	replaced = replace.replace('ineedhelp', 'e', 'xo')
	should_be = 'inxoxodhxolp'
	is_correct = True if replaced == should_be else False
	if not is_correct:
		failed += 1
	print(f'should be: {should_be} | replaced: {replaced} | replaced {"=" if is_correct else "!"}= should be')

	return failed

main()