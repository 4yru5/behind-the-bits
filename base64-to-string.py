import base64

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def decode_base64(value):
    value = "".join(value.split()).replace("-", "+").replace("_", "/")
    if len(value) % 4 == 1:
        raise ValueError("Invalid Base64 length.")
    value += "=" * (-len(value) % 4)
    return value, base64.b64decode(value, validate=True)


encoded = input("Enter a Base64 value: ")

try:
    normalized, data = decode_base64(encoded)
except (ValueError, base64.binascii.Error) as error:
    print(f"Invalid Base64: {error}")
else:
    print("\nBlock  Base64  6-bit values                 24-bit block")
    print("-----  ------  ---------------------------  ------------------------")

    for start in range(0, len(normalized), 4):
        chunk = normalized[start:start + 4]
        padded = chunk.ljust(4, "=")
        values = [ALPHABET.index(char) if char != "=" else 0 for char in padded]
        bits = "".join(f"{value:06b}" for value in values)
        byte_count = 3 - padded.count("=")
        block_bytes = bytes(int(bits[index:index + 8], 2) for index in range(0, byte_count * 8, 8))
        print(f"{start // 4 + 1:<5}  {padded:<6}  {' '.join(f'{v:06b}' for v in values):<27}  {bits}")
        print(f"       -> bytes: {' '.join(str(byte) for byte in block_bytes)}")

    try:
        result = data.decode("utf-8")
    except UnicodeDecodeError:
        print("\nDecoded bytes are not valid UTF-8 text:")
        print(data)
    else:
        print("\nResulting string for the Base64 value is:")
        print(result)
