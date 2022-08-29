from replace import replace

def main():
	failed = 0
	print(f'\nRunning Replace version {replace.__version__}')

	original = 'test'
	replaced = replace.replace('test', 't', 's')
	should_be = 'sess'
	is_correct = True if replaced == should_be else False
	if not is_correct:
		failed += 1
	print(f'original: {original} | should be: {should_be} | replaced: {replaced} | replaced {"=" if is_correct else "!"}= should be')

	original = 'ineedhelp'
	replaced = replace.replace(original, 'ed', 'x')
	should_be = 'inxxxhxlp'
	is_correct = True if replaced == should_be else False
	if not is_correct:
		failed += 1
	print(f'original: {original} | should be: {should_be} | replaced: {replaced} | replaced {"=" if is_correct else "!"}= should be')

	original = 'mylasttest'
	replaced = replace.replace(original, 't', '')
	should_be = 'mylases'
	is_correct = True if replaced == should_be else False
	if not is_correct:
		failed += 1
	print(f'original: {original} | should be: {should_be} | replaced: {replaced} | replaced {"=" if is_correct else "!"}= should be')

	return failed

main()