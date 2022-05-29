import time

def another():
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
        choose = int(input("You: "))
        while 1:
            if choose == 1:
                time.sleep(1)
                print("Great, now enter a decimal number: ")
                num = int(input("Number: "))
                print(decimal_to_binary(num))
                time.sleep(1)        
                another()
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
    except ValueError:
        print("Enter a numeric value! (1/2)")
        choose_program()



def decimal_to_binary(num):
    lst = []

    while (num != 0):
        x = num % 2
        lst.append(x)
        num = num//2

    lst.reverse()
    result = ""
    for i in lst:
        result += str(i)

    return result

def binary_to_decimal(num):
    i = 0
    result = 0

    while num != 0:
        x = num % 10
        x = x * 2**i
        i += 1
        result += x
        num = num // 10

    return result


choose_program()