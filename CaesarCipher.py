# This is a comment - it is ignored when the code is run
# Comments tell the reader what the code is doing

# Define the secret message
message = "This is a secret message"

# OR Use a message given by the user
# Remove the # from the line below to use it
#message = input("Enter a message")

# Define how much we are shifting the letters by
shift = 1
encrypted = ""

# Encrypt each letter one at a time
for letter in message:
    ascii_value = ord(letter)
    ascii_value = ascii_value + shift
    new_letter = chr(ascii_value)
    encrypted += new_letter

# Display the new message after encoding
print(encrypted)


