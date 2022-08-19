'''
capitalizes all lowercase characters in a string
'''

__version__ = '2.0.0'

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'


def make_upper(upper_string: str):
	'''
	capitalizes all lowercase characters in a string
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


def make_lower(lower_string: str):
	'''
	makes all uppercase characters in a string lowercase.
	also added just for fun c:
	'''

	if not isinstance(lower_string, str):
		raise ValueError(f'A string is needed, not {type(lower_string).__name__}')

	string_location = 0
	for character in lower_string:
		if character in uppercase:
			location = 0
			for look_in_lowercase in uppercase:
				if look_in_lowercase == character:
					break
				else:
					location += 1
			lower_string = lower_string[:string_location] + lowercase[location] + lower_string[string_location+1:]
		string_location += 1

	return lower_string
