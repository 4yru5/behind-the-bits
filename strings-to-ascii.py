text = input("Enter a string: ")

print()
print(f"{'Char':<8}ASCII")
print(f"{'----':<8}-----")

codes = []
for char in text:
    code = ord(char) 
    if code > 127:
        print(f"{repr(char):<8}not ASCII")
        continue
    codes.append(code)
    print(f"{repr(char):<8}{code}")

print()
print(f"Input   : {text}")
print(f"Bytes   : {len(codes)}")
print(f"ASCII   : {' '.join(str(c) for c in codes)}")
