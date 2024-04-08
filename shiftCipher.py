# making shift cipher encryption and decryption using python

domain = 26
string = "abcdefghijklmnopqrstuvwxyz"

userInput = input("Enter your text: ")
key = int(input("Enter the key: "))
userInput = userInput.lower()

def encryption(userInput, key, domain, string):
    
    cipher = ""
    for i in range(len(userInput)):
        for j in range(len(string)):
            if string[j] == userInput[i]:
                text = (string[(j+key)%domain])
                cipher = cipher + text
                
    print(cipher)

encryption(userInput, key, domain, string)
