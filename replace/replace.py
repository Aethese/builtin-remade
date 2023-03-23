__version__ = '1.0.0'

def replace(input_string: str, character_changing: str, new_character: str):
	'''
	replaces a character or characters in a string with a different character.
	unlike Python's version of replace, my version supports changing multiple
	characters at once

	Parameters
	----------
	input_string : str
		string that is being changed
	character_changing : str
		the character that is being changed. multiple characters can be fit
		into a single line without any separators
	new_character : str(char)
		the new character replacing the character that is changing. NEEDS to be
		a single character. if the length is bigger than 1, it limits itself to
		the first character automatically. it also can't be a blank space
	'''

	if not isinstance(input_string, str):
		raise ValueError(f'A string is needed, not {type(input_string).__name__}')

	if new_character == '':
		raise ValueError('new_character can\'t be an empty string')

	if len(new_character) > 1:
		new_character = new_character[0]

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
