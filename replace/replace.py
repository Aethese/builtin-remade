__version__ = '0.1.0'

def replace(input_string: str, character_changing: str, new_character: str):
	'''
	replaces a character or characters in a string with a different character

	Parameters
	----------
	input_string : str
		string that is being changed
	character_changing : str
		the character that is being changed. multiple characters can be fit
		into a single line without any separators
	new_character : str(char)
		the new character replacing the character that is changing. should be
		a single character or a string
	'''

	if not isinstance(input_string, str):
		raise ValueError(f'A string is needed, not {type(input_string).__name__}')

	string_location = 0
	for character in input_string:
		if character in character_changing:
			location = 0
			for look_in_string in character_changing:
				if look_in_string == character:
					break
				else:
					location += 1
			input_string = input_string[:string_location] + new_character + input_string[string_location+1:]
		string_location += 1

	return input_string