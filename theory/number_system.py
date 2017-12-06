#dec is a number
def dec2bin(dec):
	result = ""

	while dec != 0:
		result = result + str(dec % 2)
		dec = int(dec / 2)

	return result[::-1]

#bin is a string
def bin2dec(bin):
	dec = 0
	length = len(bin)
	for idx in range(length-1, -1, -1):
		dec = dec + int(bin[length - 1 - idx]) * (2 ** idx)

	return dec

#hex is a string, A-F uppercase
def hex2dec(hex):
	dec = 0
	length = len(hex)
	for idx in range(length-1, -1, -1):
		ascii_code = ord(hex[length - 1 - idx])
		if ascii_code in range(65, 71):
			num = ascii_code - 55
		else:
			num = int(hex[length - 1 - idx])
		dec = dec + num * (16 ** idx)
	return dec

def dec2hex(dec):
	result = ""
	while dec != 0:
		remainder = dec % 16
		char = str(remainder)
		if remainder >= 10:
			char = chr(remainder + 55) 
		result = result + char
		dec = int(dec / 16)

	return result[::-1]	

def hex2bin(hex):
	return (hex2dec(hex))

def bin2hex(bin):
	return dec2hex(bin2dec(bin))


print(hex2bin("FF"))