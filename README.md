# 🔤 Morse Code Converter

A simple Python project that converts text into **Morse code**. The program can take input either from a `.txt` file or directly from the user and saves the converted Morse code into a new text file.

## ✨ Features

- 🔤 Converts letters (`A-Z`) into Morse code
- 🔢 Supports numbers (`0-9`)
- ✍️ Supports punctuation marks
- 🌍 Supports several extended/accented characters
- 📄 Takes input from a `.txt` file
- ⌨️ Takes input directly as a string
- 💾 Saves the converted Morse code to `morse_output.txt`
- ⚠️ Handles invalid menu choices with an error

## 🛠️ Technologies Used

- Python
- File Handling
- Dictionary
- Functions
- String Methods
- Exception Handling

## 📂 Project Structure

```text
Morse-Code-Converter/
│
├── main.py
├── User.txt
├── morse_output.txt
└── README.md
```

## 🚀 How It Works

The program first asks how you want to provide the input:

```text
1: Text file
2: String
```

### Option 1: Text File

If you choose `1`, the program reads the content from `User.txt` and converts it into Morse code.

Example `User.txt`:

```text
Hello World
How are you?
```

The converted Morse code is then saved in:

```text
morse_output.txt
```

### Option 2: String

If you choose `2`, you can directly enter a sentence:

```text
Enter your sentence to convert to Morse code:
```

The program converts the sentence and saves the result to `morse_output.txt`.

## 📌 Example

### Input

```text
Hello World
```

### Output

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

## 📖 Morse Code Mapping

The project uses a Python dictionary to store the relationship between characters and their Morse codes.

For example:

```python
"A": ".-",
"B": "-...",
"C": "-.-.",
"0": "-----",
"1": ".----"
```

A space between words is represented using:

```python
" ": "/"
```

## 💾 Output

After conversion, the Morse code is saved in:

```text
morse_output.txt
```

The program also displays the converted Morse code in the terminal.

## ▶️ How to Run

Clone the repository and run the Python file:

```bash
python main.py
```

Then select your preferred input method.

## 🎯 Purpose

This project was created to practice:

- Python dictionaries
- Loops
- Functions
- String handling
- File reading and writing
- Basic error handling
