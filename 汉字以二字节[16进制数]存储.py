from array import array
a = array('H', [0x4e00, 0x5577, 0x9fa5])
print(chr(a[0]), chr(a[1]), chr(a[2]))
print(hex(ord('一')))
print(hex(20902+0x4e00))
print(hex(ord('项')))
print(hex(ord('道')))
print(hex(ord('德')))
