
# 📄 File Handling Tasks in Python

This repository contains two Python scripts that demonstrate basic **file handling operations**. These tasks focus on opening, reading, appending, and displaying file contents using Python’s built-in file handling functions.

---

## 📝 Task 1: Read File Line by Line

### ✅ Description

This Python function reads the content of a text file **line by line** and prints each line along with its line number. If the file is not found, it handles the error gracefully by displaying an appropriate message.

### 🔧 Code:

```python
def read_file_line_by_line(filename):
    try:
        with open(filename, 'r') as file:
            print('Reading file content: ')
            for line_number, line in enumerate(file, start=1):
                print(f'Line {line_number}: {line.strip()}')
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
```

### 🔍 How It Works:

1. **`def read_file_line_by_line(filename):`**  
   Defines a function that accepts a filename as an argument.

2. **`try:` block**  
   Used to catch exceptions like `FileNotFoundError`.

3. **`with open(filename, 'r') as file:`**  
   Opens the file in read mode. The `with` statement ensures the file is properly closed after the block is executed.

4. **`enumerate(file, start=1)`**  
   Loops through each line in the file and returns the line along with its line number (starting from 1).

5. **`line.strip()`**  
   Removes any leading/trailing whitespace and newline characters from each line before printing.

6. **`except FileNotFoundError:`**  
   If the file doesn’t exist, a custom error message is shown.

### 💡 Example Usage:

```python
read_file_line_by_line('sample.txt')
```

---

## 📝 Task 2: Append to a File and Display Final Content

### ✅ Description

This Python script appends user input to a file and displays the complete contents of the file after appending. It demonstrates **appending mode**, **user input handling**, and **reading from the file** to show the updated content.

### 🔧 Code:

```python
def file_append(filename):
    with open(filename, 'a') as file:
        input1 = input('Enter text to write to the file: ')
        file.write(input1 + '\n')
        print(f'Data successfully written to the {filename}.\n')

        input2 = input('Enter additional text to append: ')
        file.write(input2 + '\n')
        print('Data successfully appended.\n')

    print(f'Final contents of {filename}')
    with open(filename, 'r') as file:
        print(file.read())
```

### 🔍 How It Works:

1. **`def file_append(filename):`**  
   Defines a function that takes the filename where data will be appended.

2. **`with open(filename, 'a') as file:`**  
   Opens the file in append mode (`'a'`). This allows adding new content at the end without modifying existing data.

3. **`input()`**  
   Prompts the user to enter text. The input is then written to the file followed by a newline character `\n`.

4. **`file.write(input1 + '\n')`**  
   Appends the input string and a newline to the file.

5. **`print()` statements**  
   Confirms that data has been successfully added.

6. **Re-opening the file in read mode**  
   To show the complete contents of the file after appending the inputs.

7. **`file.read()`**  
   Reads and prints all content from the file.

### 💡 Example Usage:

```python
file_append('output.txt')
```
