text = input("Enter a string: ")

print()
print(f"{'Char':<8}{'ASCII':<8}Binary")
print(f"{'----':<8}{'-----':<8}------")

bits = []
for char in text:
    code = ord(char)                 # character -> ASCII number
    if code > 127:
        print(f"{repr(char):<8}not ASCII")
        continue
    binary = format(code, "08b")     # ASCII number -> 8 bits (1s and 0s)
    bits.append(binary)
    print(f"{repr(char):<8}{code:<8}{binary}")

print()
print(f"Input   : {text}")
print(f"Bits    : {len(bits) * 8}")
print(f"Binary  : {' '.join(bits)}")

places = [128, 64, 32, 16, 8, 4, 2, 1]

print()
print("How the bits add up:")
for char in text:
    code = ord(char)
    if code > 127:
        continue
    binary = format(code, "08b")
    used = [str(p) for p, b in zip(places, binary) if b == "1"]
    print()
    print(f"{repr(char)} = {code}")
    print("  Place : " + " ".join(f"{p:>3}" for p in places))
    print("  Bit   : " + " ".join(f"{b:>3}" for b in binary))
    print(f"  Sum   : {' + '.join(used)} = {code}")
