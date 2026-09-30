morse_code = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",

    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}

print("Converting file from .txt or by using string")
choise=int(input("1: for .txt and 2 : for String = "))

def converter(User_string):
    morf_code=''
    for word in User_string:
        cap_word=word.upper()
        if cap_word in morse_code:
            morf_code +=morse_code[cap_word]
    with open("mof_output.txt",'w') as file:
        file.write(morf_code)
    return morf_code

if choise== 1:
    with open('a.txt','r') as file:
        main=file.read()
        ouput_fn=converter(main)
        print(ouput_fn)

elif choise ==2:
    User_string=input("Enter you Sentence for converting in Morfing:")
    ouput_fn=converter(User_string)
    print(ouput_fn)

else:
    raise ValueError("YOU ENTER THE WRRONG VALUE")
