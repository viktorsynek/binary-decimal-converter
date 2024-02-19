############################################   -== INFORMATION ==-   ############################################

#### THE PROGRAM WAS CREATED AND PUBLISHED BY:
#### https://github.com/viktorsynek
#### https://www.linkedin.com/in/viktor-synek/

#############################################   -== PROGRAM ==-   ###############################################

#IMPORT LIBRARIES
import time

def another():
    # IF USER INPUTS "N" THE PROGRAM STOPS
    print("Do you want to convert another? (Y/N)")
    another = input("Input: ").lower()
    
    while another != "n" and another != "y":
        another = input("Input: ").lower()

    choose_program() if another == "y" else exit()

def choose_program():
    time.sleep(1)
    print("Which program you want to use?")
    time.sleep(1)
    print("1.Decimal to Binary")
    time.sleep(1)
    print("2.Binary to Decimal")
    time.sleep(2)
    print("Type: 1 if the first one, 2 if the second one!")
    try:
        # USER GIVES WHICH PROGRAM DO THEY WANT TO WORK WITH (1/2)
        choose = int(input("You: "))
        while 1:
            # DECIMAL -> BIN
            if choose == 1:
                time.sleep(1)
                print("Great, now enter a decimal number: ")
                num = int(input("Number: "))
                print(decimal_to_binary(num))
                time.sleep(1)        
                another()
            # BIN -> DECIMAL
            elif choose == 2:
                time.sleep(1)
                print("Great, now enter a binary number:")
                num = int(input("Number: "))
                print(binary_to_decimal(num))
                time.sleep(1)
                another()
            else:
                print("Enter 1 or 2!")
                choose = int(input("You: "))
                continue
    # HANDLE NOT NUMERIC INPUTS
    except ValueError:
        print("Enter a numeric value! (1/2)")
        choose_program()


# DECIMAL -> BINARY WITHOUT BUILT-IN FUNCTIONS
def decimal_to_binary(num):
    result = ""
    while num > 0:
        remainder = num % 2
        result = str(remainder) + result
        num //= 2
    return result
    
# BINARY -> DECIMAL WITHOUT BUILT-IN FUNCTIONS
def binary_to_decimal(num):
    result = 0
    i = 0
    while num > 0:
        result += (num % 10) << i
        num //= 10
        i += 1
    return result


choose_program()
