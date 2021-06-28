import bindec


def charToBin(c):
    c = str(c)
    if c.isalpha():
        if "A" <= c <= "Z":
            return bindec.decToBin(ord(c) - 65)

        if "a" <= c <= "z":
            return bindec.decToBin(ord(c) - 71)

    elif c == "+":
        return [1, 1, 1, 1, 1, 0]
    elif c == "/":
        return [1, 1, 1, 1, 1, 1]

    if c.isdigit():
        return bindec.decToBin(int(c) + 52)


def binToChar(b):
    if 0 <= bindec.binToDec(b) <= 25:
        return chr(bindec.binToDec(b) + 65)
    elif 26 <= bindec.binToDec(b) <= 51:
        return chr(bindec.binToDec(b) + 71)
    elif 52 <= bindec.binToDec(b) <= 61:
        return bindec.binToDec(b) - 52
    elif bindec.binToDec(b) == 62:
        return "+"
    elif bindec.binToDec(b) == 63:
        return "/"


def strToBin(s):
    list = []
    for chr in s:
        list += charToBin(chr)
    return list


def binToStr(b_list):
    count = 0
    list = []
    string = ""
    for element in b_list:
        list.append(element)
        count += 1
        if count == 6:
            string += str(binToChar(list))
            count = 0
            list = []
    return string


def generatePad(seed, k, l):
    list = []
    for i in range(l):
        if seed[0] == seed[len(seed) - k]:
            xor = 0
        else:
            xor = 1
        list.append(xor)
        seed.pop(0)
        seed.append(xor)
    return list


def encrypt(message, seed, k):
    key = generatePad(seed, k, 6 * len(message))
    encoded_Message = strToBin(message)
    encoded_cihertext = []
    for i in range(len(encoded_Message)):
        if key[i] == encoded_Message[i]:
            xor = 0
        else:
            xor = 1
        encoded_cihertext.append(xor)
    ciphertext = binToStr(encoded_cihertext)
    return ciphertext