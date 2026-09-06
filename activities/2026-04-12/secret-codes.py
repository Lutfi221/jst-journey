print('Welcome to the language encryptor!')

lang_encrypt={

         
    'a':'b',
    'b':'c',
    'c':'d',
    'd':'e',
    'e':'f',
    'f':'g',
    'g':'h',
    'h':'i',
    'i':'j',
    'j':'k',
    'k':'l',
    'l':'m',
    'm':'n',
    'n':'o',
    'o':'p',
    'p':'q',
    'q':'r',
    'r':'s',
    's':'t',
    't':'u',
    'u':'v',
    'v':'w',
    'w':'x',
    'x':'y',
    'y':'z',
    'z':'a'


}
iterations = int(input("How many times you want it shifted?"))

message=input('What is your message? ')

encrypted_message = ""

for i in range(iterations):
    for char in message:
        x=lang_encrypt[char.lower()]
        encrypted_message=encrypted_message+x

    message = encrypted_message
    encrypted_message = ""

print(message)