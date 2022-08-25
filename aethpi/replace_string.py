def replace_string(input_string: str, character_replace: str,
					replace_with: str, return_str: bool):
	'''
	replaces a character in a string and returns new string
	or the index of the character

	Parameters
	----------
	input_string : str

	character_replace : str
		the character needing replaced
	replace_with : str
		the character to be replaced with
	return_str : bool
		determines if a string is returned. if False, returns index of character
	'''

	string_location = 0
	for character in input_string:
		if character in character_replace:
			location = 0
			for look_in_str in character_replace:
				if look_in_str == character:
					break
				else:
					location += 1
			input_string = input_string[:string_location] + replace_with + input_string[string_location+1:]
		string_location += 1

	return input_string if return_str else string_location