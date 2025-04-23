

def read_file_line_by_line(filename):

    try:
        with open(filename,'r') as file:
            print('Reading file content: ')
            for line_number, line in enumerate(file, start = 1):
                print(f'Line {line_number}: {line.strip()}')
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


read_file_line_by_line('sample.txt')

