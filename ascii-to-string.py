def split_codes(digits):
    """Choose a printable ASCII split for an unseparated digit string."""
    best = [None] * (len(digits) + 1)
    best[0] = (0, 0, ())

    for start in range(len(digits)):
        if best[start] is None:
            continue
        controls, length_score, codes = best[start]
        for end in range(start + 1, min(start + 3, len(digits)) + 1):
            part = digits[start:end]
            code = int(part)
            if code > 127 or (len(part) > 1 and part[0] == "0"):
                continue
            char = chr(code)
            candidate = (
                controls + (not char.isprintable()),
                length_score - len(part),
                codes + (code,),
            )
            if best[end] is None or candidate[:2] < best[end][:2]:
                best[end] = candidate

    return None if best[-1] is None else best[-1][2]


text = input("Enter ASCII decimal codes: ").strip()
codes = None

if not text:
    codes = ()
elif not all(char in "0123456789" or char.isspace() for char in text):
    print("Use decimal ASCII codes with optional spaces.")
elif len(text.split()) > 1:
    values = text.split()
    if all(len(value) <= 3 and int(value) <= 127 for value in values):
        codes = tuple(map(int, values))
    else:
        print("Each ASCII code must be between 0 and 127.")
else:
    codes = split_codes(text)
    if codes is None:
        print("Could not split the digits into ASCII codes from 0 to 127.")

if codes is not None:
    decoded = "".join(map(chr, codes))
    print("\nASCII  Character")
    print("-----  ---------")
    for code in codes:
        print(f"{code:<6}  {chr(code)!r}")
    print("\nResulting string for the ASCII values is:")
    print(decoded)
