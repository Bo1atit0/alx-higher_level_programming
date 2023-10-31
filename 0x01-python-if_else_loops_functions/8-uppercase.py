def uppercase(str):
    result = ""  # empty string to store uppercase characters
    for ch in str:
        c = ord(ch)
        if c >= ord("a") and c <= ord("z"):
            ch = chr(c - 32)
        result = result + ch
    print(result, end="")
    print()
