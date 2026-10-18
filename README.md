# Behind the Bits

Scripts that show how text is represented by computers.

- `string-to-ascii.py` prints each character's ASCII value.
- `string-to-binary.py` shows each character's 8-bit binary form and how its bits add up.
- `string-to-base64.py` shows how UTF-8 bytes are grouped and encoded as Base64.

## Run

Requires Python 3. From the repository directory:

```bash
python3 string-to-ascii.py
python3 string-to-binary.py
python3 string-to-base64.py
```

Enter a string when prompted. The ASCII and binary scripts identify characters outside the ASCII range as `not ASCII`.
