'''
upper will make all characters in the alphabet capitalized
'''

__version__ = '1.0.0'

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'

def make_upper(upper_string: str):
	'''
	how it works: it will go through all of the characters in the string. if the character
	the for loop goes through is in the `lowercase` var, meaning its a lowercase character.
	then after its figured it out that's a 
	'''

	if not isinstance(upper_string, str):
		raise ValueError(f'A string is needed, not {type(upper_string).__name__}')

	string_location = 0
	for character in upper_string:
		if character in lowercase:
			location = 0
			for look_in_lowercase in lowercase:
				if look_in_lowercase == character:
					break
				else:
					location += 1
			upper_string = upper_string[:string_location] + uppercase[location] + upper_string[string_location+1:]
		string_location += 1

	return upper_string
