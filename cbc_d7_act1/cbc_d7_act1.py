def create_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
        print(f'File {filename} created with content.')


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print('File Content:\n', content)
    except FileNotFoundError:
        print('File not found!')


def update_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f'File {filename} updated with new content.')
    except FileNotFoundError:
        print('File not found!')


def delete_file(filename):
    import os
    try:
        os.remove(filename)
        print(f'File {filename} deleted.')
    except FileNotFoundError:
        print('File not found!')


def main():
    while True:
        print('\n1. Create File\n2. Read File\n3. Update File\n4. Delete File\n5. Exit')
        choice = input('Choose an option: ')
        if choice == '1':
            filename = input('Enter the filename to create: ')
            content = input('Enter content for the file: ')
            create_file(filename, content)
        elif choice == '2':
            filename = input('Enter the filename to read: ')
            read_file(filename)
        elif choice == '3':
            filename = input('Enter the filename to update: ')
            content = input('Enter content to update: ')
            update_file(filename, content)
        elif choice == '4':
            filename = input('Enter the filename to delete: ')
            delete_file(filename)
        elif choice == '5':
            print('Exiting...')
            break
        else:
            print('Invalid choice!')

if __name__ == '__main__':
    main()
