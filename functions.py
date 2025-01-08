def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content 

if __name__ == "__main__":
    read_file('text.txt')