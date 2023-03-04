def MTA():
	while True:
		message = input('\nMTA please enter msg(enter to exit): ').strip()
		if message == '':
			break
		print(decode_morse_code(message))

def atm():
	while True:
		message = input('\nATM please input msg(enter to exit): ')
		if message == '':
			break
		print(encode_to_morse_code(message))

def encode_to_morse_code(message):
    # define morse code lookup table
    morse_code = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
        'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
        '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
        '@': '.--.-.', '=': '-...-', "'": '.----.', '!': '-.-.--',
        ';': '-.-.-.', '+': '.-.-.', ':': '---...', '{': '-.--.',
        '}': '-.--.-', '&': '.-...'
    }

    # convert message to lowercase
    message = message.lower()

    # encode message to Morse code
    encoded_message = []
    for char in message:
        if char == ' ':
            encoded_message.append('/')
        else:
            encoded_message.append(morse_code.get(char, ''))
    return ' '.join(encoded_message)
    
    
    
    
    
def decode_morse_code(message):
    # define morse code lookup table
    morse_code = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
        '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
        '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
        '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
        '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
        '--..': 'z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
        '-----': '0', '--..--': ',', '.-.-.-': '.', '..--..': '?',
        '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')',
        '.--.-.': '@', '-...-': '=', '.----.': "'", '-.-.--': '!',
        '-.-.-.': ';', '-...-': '=', '-....-': '-', '..--.-': '_', 
        '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '.-.-.': '+', 
        '.-.-.': '+', '---...': ':', '-.-.-.': ';', '-.--.': '{',
        '-.--.-': '}', '.-...': '&'
    }

    # split the message into words and then letters
    words = message.strip().split(' / ')
    decoded_message = []
    for word in words:
        letters = word.split(' ')
        decoded_word = ''
        for letter in letters:
            decoded_word += morse_code.get(letter, '')
        decoded_message.append(decoded_word)
    return ' '.join(decoded_message)
    
while True:
	print('press 1 for Morse To Alpha')
	print('press 2 for Alpha To Morse')
	select = input('Select Function(enter to exit): ')
	if select == '1':
		MTA()
	elif select == '2':
		atm()
	elif select == '':
		break
	else:
		print('\nEngine Failure\n')
