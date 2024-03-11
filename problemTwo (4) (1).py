# Student: Adel Ahmed Mohammed El Hefny ID: 20230198
# Student: Ahmed Mohammed Mahmoud Ahmed ID: 20230598
# Student: Ahmed Hussein Ahmed Mohammed Salh ID: 20230015

def exitMenu():
    print("** binary calculator **")
    print("A) Insert new numbers")
    print("B) Exit")
    return input("Please enter your choice (A/B): ")
def operationMenu():
    print("A) Compute one's complement")
    print("B) Compute two's complement")
    print("C) addition")
    print("D) subtraction")
    return input("Please enter your choice (A/B/C/D): ")
def oneComplement(binaryNumber):
    comp=["1","0"]
    result=''
    while (binaryNumber > 0):
        rem= binaryNumber %2
        result=comp[rem] + result
        binaryNumber=binaryNumber//10
    return result
def twoComplement(binaryNumber):
    num_list = list(binaryNumber)  # Convert the string to a list of characters
    size = len(num_list)
    x = 0
    for i in range(size-1, -1, -1):
        if x == 0:
            if num_list[i] == '1':
                x = 1
        else:
            if num_list[i] == '1':
                num_list[i] = '0'
            else:
                num_list[i] = '1'
    twos_comp = ''.join(num_list)
    return twos_comp
def addition(num1,num2):
    while len(num1) > len(num2):
        num2 = "0" + num2  # Add leading zeros to the two numbers of equivalent length
    while len(num2) > len(num1):
        num1 = "0" + num1  # Add leading zeros to the two numbers of equivalent length
    carry = "0"
    Bin_Add = ""  # create empty string in order to fill it later with result digits
    for index in range(len(num1)-1, -1, -1):  # loop on string from the right
        Dec_Sum = int(num1[index]) + int(num2[index]) + int(carry)  # Add digits of num1,num2 and carry
        if Dec_Sum == 0:
            carry = "0" ; bit = "0"
        elif Dec_Sum == 1 :
            carry = "0" ; bit = "1"
        elif Dec_Sum == 2:
            carry = "1" ; bit = "0"
        else:
            carry = "1" ; bit = "1"
        if index == 0 and carry == "1":
            Bin_Add = carry + bit + Bin_Add  # when index=0 and carry = 1 , carry wil be concatenated
        else:
            Bin_Add = bit + Bin_Add  # fill the  empty string with bits
    return Bin_Add
def subtraction(num1,num2):
    num1 = str(num1)
    num2 = str(num2)
    # here we are checking if the length of the second number equal to length of the first one if not we fill it with zeros
    if(len(num2) < len(num1)):
        index = len(num2)
        while(index < len(num1)):
            num2 = '0' + num2
            index += 1
    result = ""
    index = len(num1) - 1
    # looping in the two numbers and checking if the digit we at now are 0 and 1 or not
    # if they are 0 and 1 we try to find "1" in the first number precedes our zero to borrow from it
    # if they are not 0 and 1 we simply subtract them
    while(index >= 0):
        if(num1[index] == '0' and num2[index] == '1'):
            found = False
            index2 = index - 1
            while(index2 >= 0):
                if(found):
                    if(index2 == index):
                         # here makeing new string with updated value
                        newNum1 = ""
                        for index3,item in enumerate(num1):
                            if(index3 == index):
                                newNum1 += '2'
                            else:
                                newNum1 += num1[index3]
                        num1 = newNum1
                        break
                    else:
                        # here makeing new string with updated value
                        newNum1 = ""
                        for index3,item in enumerate(num1):
                            if(index3 == index2):
                                newNum1 += '1'
                            else:
                                newNum1 += num1[index3]
                        num1 = newNum1
                    index2 += 1
                else:
                    if(num1[index2] == '1'):
                         # here makeing new string with updated value
                        newNum1 = ""
                        for index3,item in enumerate(num1):
                            if(index3 == index2):
                                newNum1 += '0'
                            else:
                                newNum1 += num1[index3]
                        num1 = newNum1
                        found = True
                        index2 += 2
                    index2 -= 1
            result = str(int(num1[index]) - int(num2[index])) + result
        else:
            result = str(int(num1[index]) - int(num2[index])) + result
        index -= 1
    return result
# print(subtraction("01010101010101","111")) result 01010101001110
# print(subtraction("111","111")) result 000
# print(subtraction("101111100100101001111001111101011011010101010111111111011111111","1")) result 101111100100101001111001111101011011010101010111111111011111110
# print(subtraction("1","1")) result 0
# print(subtraction("1","0")) result 1
# print(subtraction("0","0")) result 0
# print(subtraction("1111111111","111111111")) result 1000000000

while(True):
    num1 = 0
    num2 = 0
    condition = False # checks if user wants to close the program or not
    while(True):
        result = exitMenu()
        if(result.lower() == 'a'):
            num1 = input("Please insert a number: ")
            checker = False # To check if the user entered a proper number or not
            for char in num1: # checking if the user entered a base 2 number
                if(char != '0' and char != '1'):
                    checker = True 
                    break
            if(checker):
                print("please insert a valid binary number")
                continue
            break
        elif(result.lower() == 'b'):
            condition = True
            break
        else:
            print("Invalid choice please try again")
    if(condition): # the user chosed B as his choice
        break
    operation = 0
    num2 = 0
    while(True):
        result = operationMenu().lower()
        if(result == 'a'):
            operation = 1
            break
        elif(result == 'b'):
            operation = 2
            break
        elif(result == 'c'):
            operation = 3
            while(True):
                checker = False
                num2 = input("insert the second number: ")
                for char in num2: # checking if the user entered a base 2 number
                    if(char != '0' and char != '1'):
                        checker = True 
                        break
                if(checker):
                    print("Please enter a valid base 2 number")
                    continue
                break
            break
        elif(result == 'd'):
            operation = 4
            while(True):
                checker = False
                num2 = input("Enter Second Number: ")
                for char in num2: # checking if the user entered a base 2 number
                    if(char != '0' and char != '1'):
                        checker = True 
                        break
                if(checker):
                    print("Please enter a valid base 2 number")
                    continue
                break
            break
        else:
            print("Invalid choice please try again")
    if(operation == 1):
        result = oneComplement(int(num1))
        print("Result is: " + str(result))
    elif(operation == 2):
        result = twoComplement(num1)
        print("Result is: " + str(result))
    elif(operation == 3):
        result = addition(num1,num2)
        print("Result is: " + str(result))
    elif(operation == 4):
        result = subtraction(num1,num2)
        print("Result is: " + str(result))
    