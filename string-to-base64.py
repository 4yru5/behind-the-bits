text = input("Enter a string: ") 

# Base64 encodes bytes, so convert the text to UTF-8 first. 
data = text.encode("utf-8")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

encoded = []

print()
print(f"Input       : {text}")
print(f"UTF-8 bytes : {len(data)}")

if data:
    print()
    print(
        f"{'ASCII':<18}"
        f"{'24-bit block':<30}"
        f"{'6-bit groups':<30}"
        f"{'Base64':<10}"
    )
    print(
        f"{'-----':<18}"
        f"{'------------':<30}"
        f"{'------------':<30}"
        f"{'------':<10}"
    )

for start in range(0, len(data), 3):
    chunk = data[start:start + 3]

    # Pad the final block with zero bytes for the calculation.
    padded = chunk + b"\x00" * (3 - len(chunk))
    block = int.from_bytes(padded, "big")

    # Split the 24-bit block into four 6-bit values.
    values = [
        (block >> 18) & 0b111111,
        (block >> 12) & 0b111111,
        (block >> 6) & 0b111111,
        block & 0b111111,
    ]

    # Convert each 6-bit value to a Base64 character.
    chars = [alphabet[value] for value in values]

    # Use "=" for groups that came from padding bytes.
    if len(chunk) == 1:
        chars[2:] = ["=", "="]
    elif len(chunk) == 2:
        chars[3] = "="

    encoded_text = "".join(chars)
    encoded.append(encoded_text)

    byte_text = " ".join(str(byte) for byte in chunk)
    binary_block = format(block, "024b")
    groups = " ".join(format(value, "06b") for value in values)

    print(
        f"{byte_text:<18}"
        f"{binary_block:<30}"
        f"{groups:<30}"
        f"{encoded_text:<10}"
    )

result = "".join(encoded)

print()
print(f"Base64      : {result}")

print()
print("How each block is calculated:")

for start in range(0, len(data), 3):
    chunk = data[start:start + 3]
    padded = chunk + b"\x00" * (3 - len(chunk))
    block = int.from_bytes(padded, "big")

    values = [
        (block >> 18) & 0b111111,
        (block >> 12) & 0b111111,
        (block >> 6) & 0b111111,
        block & 0b111111,
    ]

    chars = [alphabet[value] for value in values]

    if len(chunk) == 1:
        chars[2:] = ["=", "="]
    elif len(chunk) == 2:
        chars[3] = "="

    print()
    print(f"  ASCII : {' '.join(str(byte) for byte in chunk)}")
    print(f"  Bits  : {format(block, '024b')}")
    print(f"  Groups: {' '.join(format(value, '06b') for value in values)}")
    print(f"  Index : {'   '.join(str(value) for value in values)}")
    print(f"  Chars : {'    '.join(chars)}")
