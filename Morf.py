morse_text = {
    # Space
    " ": "/",

    # A-Z
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

    # Numbers
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",

    # Punctuation
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    ":": "---...",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    '"': ".-..-.",
    "@": ".--.-.",

    # Nonstandard punctuation
    "!": "-.-.--",
    "&": ".-...",
    ";": "-.-.-.",
    "_": "..--.-",
    "$": "...-..-",

    # Extended / accented letters
    "À": ".--.-",
    "Ä": ".-.-",
    "Å": ".--.-",
    "Ą": ".-.-",
    "Æ": ".-.-",
    "Ć": "-.-..",
    "Ĉ": "-.-..",
    "Ç": "-.-..",
    "Đ": "..-..",
    "Ð": "..--.",
    "É": "..-..",
    "È": ".-..-",
    "Ę": "..-..",
    "Ĝ": "--.-.",
    "Ĥ": "----",
    "Ĵ": ".---.",
    "Ł": ".-..-",
    "Ń": "--.--",
    "Ñ": "--.--",
    "Ó": "---.",
    "Ö": "---.",
    "Ø": "---.",
    "Ś": "...-.-",
    "Ŝ": "....-",
    "Š": "----",
    "Þ": ".--..",
    "Ü": "..--",
    "Ŭ": "..--",
    "Ź": "--..-",
    "Ż": "--..-"
}

print("Choose input method: Text file or string")
choice=int(input('1: Text file\n2: String\nEnter your choice:'))

def save_to_file(content):
    with open("morse_output.txt",'w') as file:
            file.write(content)
            
def converter(input_text):
    morf_code=''
    for word in input_text:
        strip_word=word.strip()
        for character in strip_word:
            if character == " ":
                morf_code +=morse_text[character]
            else:
                morf_code +=morse_text[character.upper()]+" "          
        morf_code+='\n'
    
    save_to_file(morf_code)
    return morf_code

if choice== 1:
    with open('User.txt','r') as file:
        file_content=file.readlines()
        output=converter(file_content)
        print(f'Code:\n{output}')

elif choice ==2:
    input_text=input("Enter your sentence to convert to Morse code:")
    output=converter(input_text)
    print(f'Code:\n{output}')

else:
    raise ValueError("Invalid choice. Please enter 1 or 2.")