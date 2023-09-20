peanuts = "On 10 May 1940, Winston Churchill became Prime Minister of the United Kingdom"
shift = 5
encrypted = ""
decrypted = ""

for char in peanuts:
    ascii_value = ord(char)

    if (ascii_value <= 65):
        first = (ascii_value + shift)
        
        encrypted += chr(first)
    else:
        first = (ascii_value + shift)
        encrypted += chr(first)

for char in encrypted:
    ascii_value = ord(char)

    if (ascii_value <= 65):
        first = (ascii_value - shift)
        
        decrypted += chr(first)
    else:
        first = (ascii_value - shift)
        decrypted += chr(first)

print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)