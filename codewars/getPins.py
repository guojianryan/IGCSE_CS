def get_pins(observed):
	meta = {"0":"08","1":"124",
	"2":"2135","3":"326","4":"4157",
	"5":"52468","6":"6359",
	"7":"748","8":"85790","9":"968"}
	keys = [meta[key] for key in observed]
	combos = [""] 
	for key_row in keys:
		combos = [ a + b for a in combos for b in key_row]
	return sorted(combos)
	
print(get_pins("369"))

