def to_lowercase(text):
    return text.lower()

def to_uppercase(text):
    return text.upper()

def to_title_case(text):
    return text.title()

def swap_case(text):
    return text.swapcase()

def capitalize_first(text):
    return text.capitalize()

while True:
    word = input("Enter a text (or type 'exit' to quit): ")
    if word.lower() == 'exit':
        print("Goodbye!")
        break
    
    print("Choose an option:")
    print("1. Lowercase")
    print("2. Uppercase")
    print("3. Title Case")
    print("4. Swap Case")
    print("5. Capitalized")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        print("Lowercase:", to_lowercase(word))
    elif choice == '2':
        print("Uppercase:", to_uppercase(word))
    elif choice == '3':
        print("Title Case:", to_title_case(word))
    elif choice == '4':
        print("Swap Case:", swap_case(word))
    elif choice == '5':
        print("Capitalized:", capitalize_first(word))
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")