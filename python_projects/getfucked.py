#Enter a list of binary and get each character printed.

binary_string =["Here is your unicode: "]
end_strings = ["end", "e"]
decimal_out = 0

def BinaryToDecimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal

while True:
    usr_input = input("Enter bianary & continue or End: ").lower()
    if usr_input in end_strings:
        break

    if usr_input.isnumeric() == True:
        if len(usr_input) == 8:
            decimal_out = BinaryToDecimal(usr_input)
            binary_string.append(chr(decimal_out))
            print("Accepted & continue.")
            continue
        else:
            print("Enter 8 bit binary only. Or End.")
    else:
        print("Enter 8 bit binary only. Or End.")

print(binary_string)
mystring=" "
for x in binary_string:
    mystring += x
print(mystring)
