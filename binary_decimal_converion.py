#Binary to Decimal and Back Converter (from https://github.com/karan/Projects) -
#Develop a converter to convert a decimal number to binary
#or a binary number to its decimal equivalent.

#method to convert binary to decimal
def binary_to_decimal(num):
    rev = str(num)[::-1]#reverse number to start from unit place
    power = 0
    decimal = 0
    while power < len(rev):
        if int(rev[power]) == 1:
            decimal += 2**power
        power += 1
    return decimal

#method to convert decimal to binary
def decimal_to_binary(num):
    binary = ''
    while int(num) > 0:
        binary += str(int(num) % 2)
        num = num / 2
    return binary[::-1]


print ("1. Binary to Decimal Conversion\n2. Decimal to Binary Conversion\n")
choice = int(input("Choose 1 or 2: "))

if choice == 1:
    num = input("Number to convert: ")
    print ("Decimal of ", num, " is ", binary_to_decimal(num))

elif choice == 2:
    num = int(input("Number to convert: "))
    print ("Binary of ", num, "is ", decimal_to_binary(num))

else:
    print ("Invalid choice")
    

