#https://www.codewars.com/kata/54b72c16cd7f5154e9000457

def decodeBits(bits):
    if len(bits) == 0: 
        return ""
    else:
        bits = bits.strip("0")
        ones_list = sorted([x for x in bits.split("0") if x != ""])
        zeros_list = sorted([x for x in bits.split("1") if x != ""])

        first_one = ones_list[0]
        last_one = ones_list[-1]

        time_unit = len(first_one)
        
        ones = "1" * time_unit
        zeros = "0" * time_unit

        if time_unit % 3 == 0:
            if len(zeros_list) > 0:
                if time_unit % len(zeros_list[0]) == 0:
                    bits =  bits.replace(ones,"1" * int((time_unit / len(zeros_list[0])))).replace(zeros, "0")
                elif len(zeros_list[0]) > time_unit and len(zeros_list[0]) % 3 == 0:
                    bits =  bits.replace(ones,"1").replace(zeros, "0")
            else:
                bits =  bits.replace(ones,"1")
        else:
            bits =  bits.replace(ones,"1").replace(zeros, "0")
        print(bits)
        return bits.replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')

def decodeMorse(morseCode):
    print("--", morseCode)
    text = ""
    for x in morseCode.split("  "):
        text = text + " " + "".join([MORSE_CODE[code] for code in x.split()])
    return text.strip()