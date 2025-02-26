def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    while True:
        user_input = input('Enter a number (or type exit to quit): ')
        if user_input.lower() == 'exit':
            print('Goodbye!')
            break
        if not user_input.isdigit():
            print('Please enter a valid number.')
            continue
        number = int(user_input)
        if is_prime(number):
            print(f'{number} is a prime number.')
        else:
            print(f'{number} is not a prime number.')

if __name__ == '__main__':
    main()
