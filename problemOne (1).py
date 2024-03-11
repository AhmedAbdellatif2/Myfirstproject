# Student: عادل احمد محمد الحفنى ID: 20230198
# Student: name 2 ID: ID2
# Student: name 3 ID: ID3

import math
def exitMenu():
    print("** numbering system converter **")
    print("A) insert a new number")
    print("B) Exit program")
    return input("Please enter your choice (A/B): ")
def FromMenu():
    print("** Please select the base you want to convert a number from**")
    print("A) Decimal")
    print("B) Binary")
    print("C) octal")
    print("D) hexadecimal")
    return input("Please enter your choice (A/B/C/D): ")
def ToMenu():
    print("** Please select the base you want to convert a number to **")
    print("A) Decimal")
    print("B) Binary")
    print("C) octal")
    print("D) hexadecimal")
    return input("Please enter your choice (A/B/C/D): ")
def binaryToDecimal(binaryNumber):
    result = 0
    index = len(binaryNumber) - 1
    for num in binaryNumber:
        result += int(num) * pow(2,index) # adding to our result the binary digit * by 2 power digit place
        index -= 1
    return result
def decimalToBinary(decimalNumber):
    result = ""
    while(True):
        result += str(decimalNumber%2) # adding reminder to result
        decimalNumber = math.floor(decimalNumber/2)
        if(decimalNumber == 0):
            break
    i = len(result) - 1 # counter
    resultInverted = ""
    while(i >= 0): # to invert the binary number
        resultInverted += result[i]
        i -= 1
    return resultInverted
def decimalToOctal(decimalNumber):
    result = ""
    while(True): # adding reminder to result
        result += str(decimalNumber%8)
        decimalNumber = math.floor(decimalNumber/8)
        if(decimalNumber == 0):
            break
    i = len(result) - 1  # counter
    resultInverted = ""
    while(i >= 0): # to invert the octal number
        resultInverted += result[i]
        i -= 1
    return resultInverted
def ocatalToDecimal(octalNumber):
    result = 0
    index = len(octalNumber) - 1
    for num in octalNumber:
        result += int(num) * pow(8,index) # adding to our result the octal digit * by 8 power digit place
        index -= 1
    return result
def hexaToDecimal(hexaNumber):
    #from hex to decimal
    hexa= hexaNumber.upper().strip()
    i=0
    dec=0
    a=0   # we need it to make sure that the number is hexa , {a} is a condition we will use it later
    length=len(hexa)-1
    while length>=0:
        if hexa[length]>='0' and hexa[length]<='9':
            reminder=int(hexa[length])
        elif hexa[length]>='A' and hexa[length]<='F':
            reminder = ord(hexa[length])-55
        else: # {a} is a break statement , if the user's input is not hexa the program will go to if statement directly
            a=a+1
            break

        dec = dec + (reminder*16**i)
        i=i+1
        length=length-1
    return dec
def decimalToHexa(decimalNumber):
    #convert from dec to hex
    hexnum={0:'0',
            1:'1',
            2:'2',
            3:'3',
            4:'4',
            5:'5',
            6:'6',
            7:'7',
            8:'8',
            9:'9',
            10:'A',
            11:'B',
            12:'C',
            13:'D',
            14:'E',
            15:'F',
    }

    dec= decimalNumber
    x=dec
    hex=''
    while dec >0 :
        rem= dec %16
        hex=hexnum[rem] +hex
        dec=dec//16
    return hex
def hexaToBinary(hexaNumber):
    decimalNumber = hexaToDecimal(hexaNumber) # covert the hexa number to decimal number
    return decimalToBinary(decimalNumber) # covert the decimal number to binary number
def binaryToHexa(binaryNumber):
    decimalNumber = binaryToDecimal(binaryNumber) # covert the binary number to decimal number
    return decimalToHexa(decimalNumber) # covert the decimal number to hexa number
def ocatalToBinary(ocatalNumber):
    binaryNumber = ocatalToDecimal(ocatalNumber) # covert the octal number to decimal number
    return decimalToBinary(binaryNumber) # covert the decimal number to binary number
def binaryToOctal(binaryNumber):
    decimalNumber = binaryToDecimal(binaryNumber) # covert the binary number to decimal number
    return decimalToOctal(decimalNumber) # covert the decimal number to octal number
def hexaToOctal(hexaNumber):
    decimalNumber = hexaToDecimal(hexaNumber) # covert the hexa number to decimal number
    return decimalToOctal(decimalNumber) # covert the decimal number to octal number
def octalToHexa(octalNumber):
    decimalNumber = ocatalToDecimal(octalNumber) # covert the octal number to decimal number
    return decimalToHexa(decimalNumber) # covert the decimal number to hexa number
while(True):
    exitCondition = False
    while(True): # to repeat the exit menu until the user continue
        exitMenuResult = exitMenu()
        if(exitMenuResult.lower() == 'a'):
            break
        elif(exitMenuResult.lower() == 'b'):
            exitCondition = True
            break
        else:
            print("please select a valid choice")
    if(exitCondition == True): # if the user chose to exit the program
        break
    ourNumber = input("please insert a Number: ")
    FromNumber = 1
    isNumberValid = True
    while(True):
        exitMenuResult = FromMenu()
        if(exitMenuResult.lower() == 'a'):
            FromNumber = 1
            # validating the number if it is a decimal or not 
            if(len(ourNumber) != 0):
                if(ourNumber[0] == '0'):
                    print("** This number is not valid for base 10 **")
                    isNumberValid = False
                    break
            for char in ourNumber:
                test = char.lower()
                if(test == 'a' or test == 'b' or test == 'c' or test == 'd' or test == 'e' or test == 'f'):
                    print("** This number is not valid for base 10 **")
                    isNumberValid = False
                    break
            break
        elif(exitMenuResult.lower() == 'b'):
            FromNumber = 2
            # validating the number if it is a binary or not 
            for char in ourNumber:
                test = char.lower()
                if(test != '0' and test != '1'):
                    print("** This number is not valid for base 2 **")
                    isNumberValid = False
                    break
            break
        elif(exitMenuResult.lower() == 'c'):
            FromNumber = 3
            # validating the number if it is a octal or not 
            if(len(ourNumber) != 0):
                if(ourNumber[0] == '0'):
                    print("** This number is not valid for base 8 **")
                    isNumberValid = False
                    break
            for char in ourNumber:
                test = char.lower()
                if(test != '0' and test != '1' and test != '2' and test != '3' and test != '4' and test != '5' and test != '6' and test != '7'):
                    print("** This number is not valid for base 8 **")
                    isNumberValid = False
                    break
            break
        elif(exitMenuResult.lower() == 'd'):
            FromNumber = 4
            # validating the number if it is a hexa decimal or not 
            if(len(ourNumber) != 0):
                if(ourNumber[0] == '0'):
                    print("** This number is not valid for base 16 **")
                    isNumberValid = False
                    break
            break
        else:
            print("please select a valid choice")
    if(isNumberValid == False): # to return back if the number is not valid
        continue
    ToNumber = 1
    while(True):
        exitMenuResult = ToMenu()
        if(exitMenuResult.lower() == 'a'):
            ToNumber = 1
            if(ToNumber == FromNumber): # to check if the user entered the same system twice
                print("please select a different choice from what you choose at the first menu")
                continue
            break
        elif(exitMenuResult.lower() == 'b'):
            ToNumber = 2
            if(ToNumber == FromNumber): # to check if the user entered the same system twice
                print("please select a different choice from what you choose at the first menu")
                continue
            break
        elif(exitMenuResult.lower() == 'c'):
            ToNumber = 3
            if(ToNumber == FromNumber): # to check if the user entered the same system twice
                print("please select a different choice from what you choose at the first menu")
                continue
            break
        elif(exitMenuResult.lower() == 'd'):
            ToNumber = 4
            if(ToNumber == FromNumber): # to check if the user entered the same system twice
                print("please select a different choice from what you choose at the first menu")
                continue
            break
        else:
            print("please select a valid choice")
    result = 0
    if(FromNumber == 1):
        if(ToNumber == 2):
            result = decimalToBinary(int(ourNumber))
        elif(ToNumber == 3):
            result = decimalToOctal(int(ourNumber))
        elif(ToNumber == 4):
            result = decimalToHexa(int(ourNumber))
    elif(FromNumber == 2):
        if(ToNumber == 1):
            result = binaryToDecimal(ourNumber)
        elif(ToNumber == 3):
            result = binaryToOctal(ourNumber)
        elif(ToNumber == 4):
            result = binaryToHexa(ourNumber)
    elif(FromNumber == 3):
        if(ToNumber == 1):
            result = ocatalToDecimal(ourNumber)
        elif(ToNumber == 2):
            result = ocatalToBinary(ourNumber)
        elif(ToNumber == 4):
            result = octalToHexa(ourNumber)
    else:
        if(ToNumber == 1):
            result = hexaToDecimal(ourNumber)
        elif(ToNumber == 2):
            result = hexaToBinary(ourNumber)
        elif(ToNumber == 3):
            result = hexaToOctal(ourNumber)
    print("The result is: " + str(result))