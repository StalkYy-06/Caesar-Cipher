import os
def welcome():
    print ('Welcome to the Caesar Cipher \nThis program encrypts and decrypts text with the Caesar Cipher.')
def enter_message():
    modes=['e','d']
    while True:
        mode = input("Type 'e' for encryption or 'd' for decryption: \n").lower()
        if mode in modes :
            break
        else:
            print("Enter Valid Mode ('e'/'d')")
    file_name,choice=message_or_file(mode)
    if choice=="file":
        process_file(file_name,mode)
        return mode,None,None
    while True:
        message = input("What message would you like to {}: ".format("encrypt" if mode == 'e' else "decrypt")).upper()
        shift = input("Enter the shift number (1-25):\n")
        if shift.isdigit() and 0<=int(shift)<=25:
            break
        else:
            print('Invalid Shift !!(1-25)') 
    return mode,message,int(shift) 
def encrypt(message,shift):
    result=""
    for char in message:
        if char.isalpha():
            result+=chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result+= char
    return result
def decrypt(message,shift):
    result=""
    for char in message:
        if char.isalpha():
            result+=chr((ord(char)-shift-65)%26+65)
        else:
            result+=char
    return result
def is_file(file_name):
    return os.path.isfile(file_name)
def process_file(file_name,mode):
    while True:
        shift = input("Enter the shift number (1-25):\n")
        if shift.isdigit() and 0<=int(shift)<=25:
            break
        else:
            print('Invalid Shift !!(1-25)')    
    with open(file_name,'r') as file:
        content=file.read().upper()
        result=None
        if mode=="e":
            result=encrypt(content,int(shift))
        elif mode=="d":
            result=decrypt(content,int(shift))
        if result is not None:
            write_message(result) 
    return None         
def message_or_file(mode):
    while True:
        fileOrMessage=input("What would you like to read from (file/message):\n").lower().strip()
        if fileOrMessage in ['file','message']:
                if fileOrMessage=='file':
                    while True:
                        file_name=input("Enter File Name : \n")
                        if is_file(file_name):
                            return file_name,"file"
                        else:
                            print("File doesnt exist. Enter a Valid Name!!")
                elif fileOrMessage=="message":
                    return None,"message"
                break
        else:
            print("Not valid form!!(file/message)")
def write_message(result):
    with open('result.txt', 'a') as output_file:
        output_file.write(result + '\n')
    print("Result saved to 'result.txt'")
def main():
    welcome()
    while True:
        mode,message,shift=enter_message()
        if message is None:
            while True:
                repeat=input("Would you like to encrypt or decrypt again? (y/n): \n").lower()
                if repeat in ['y','n']:
                    break
                else:
                    print("Enter Valid Choice!!")
            if repeat=='n':
                print("Thanks for using The Program, goodbye!")
                break
        else:
            if mode=="e":
                result=encrypt(message,shift)
                print("Encrypted Message :\n",result)
            elif mode=="d":
                result=decrypt(message,shift)
                print("Decrypted Message :\n",result)
            while True:
                repeat=input("Would you like to encrypt or decrypt again? (y/n): \n").lower()
                if repeat in ['y','n']:
                    break
                else:
                    print("Enter Valid Choice!!")
            if repeat=='n':
                print("Thanks for using The Program, goodbye!")
                break
main()