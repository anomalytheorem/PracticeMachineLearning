import base64

user_input = input("Enter binary: ")

#message_bytes = user_input

inpt_bytes = user_input.encode('utf-8')
message_bytes = base64.b64decode(inpt_bytes)
message = message_bytes.decode('utf-8')

print(message)

