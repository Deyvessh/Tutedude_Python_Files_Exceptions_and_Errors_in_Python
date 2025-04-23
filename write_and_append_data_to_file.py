
def file_append(filename):
    # Step 1: Open the file in append mode
    with open(filename, 'a') as file:
        input1 = input('Enter text to write to the file: ')
        file.write(input1 + '\n')  # Adds a newline at the end
        print(f'Data successfully written to the {filename}.\n')

        input2 = input('Enter additional text to append: ')
        file.write(input2 + '\n')  # Adds newline
        print('Data successfully appended.\n')

    # Step 2: Re-open file in read mode and display its content
    print(f'Final contents of {filename}')
    with open(filename, 'r') as file:
        print(file.read())

file_append('output.txt')


# == Output == 
# Hello, Python!
# Learning file handling in Python.

