a = (int("AAAA:BBBB:CCCC".replace(':', ''), 16))
b = bin(a)[2:]
print(b)
v = '101010101010101010111011101110111100110011001100' # искомое число
print(b == v) # if True then correct ✅
