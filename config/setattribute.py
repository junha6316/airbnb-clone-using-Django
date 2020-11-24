import sys

a = {chr(i + 65): i for i in range(26)}

for key, value in a.items():
    setattr(sys.modules[__name__], key, value)
    print(key, value)
