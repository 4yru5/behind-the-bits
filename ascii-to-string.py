def decode_concatenated(digits):
    """Split digits into ASCII values, preferring the most readable result."""
    # Dynamic programming avoids a greedy split getting stuck on an invalid
    # three-digit prefix. For ties, prefer fewer control characters, then
    # longer codes (the usual ASCII notation is two or three digits).
    best = [None] * (len(digits) + 1)
    best[0] = (0, 0, "")

    for start in range(len(digits)):
        if best[start] is None:
            continue
        controls, negative_code_lengths, decoded = best[start]
        for end in range(start + 1, min(start + 3, len(digits)) + 1):
            piece = digits[start:end]
            code = int(piece)
            if code > 127 or (len(piece) > 1 and piece.startswith("0")):
                continue
            char = chr(code)
            printable = char.isprintable()
            candidate = (
                controls + (not printable),
                negative_code_lengths - len(piece),
                decoded + char,
            )
            current = best[end]
            if current is None or candidate[:2] < current[:2]:
                best[end] = candidate

    return None if best[-1] is None else best[-1][2]


text = input("Enter ASCII codes (spaces optional): ").strip()

if not text:
    print("")
elif not all(char.isdigit() or char.isspace() for char in text):
    print("Please enter ASCII codes using digits and optional spaces.")
elif len(text.split()) > 1:
    tokens = text.split()
    if any(len(token) > 3 or int(token) > 127 for token in tokens):
        print("Please use ASCII values from 0 to 127.")
    else:
        print("".join(chr(int(token)) for token in tokens))
else:
    decoded = decode_concatenated(text)
    if decoded is None:
        print("These digits cannot be split into ASCII values from 0 to 127.")
    else:
        print(decoded)
