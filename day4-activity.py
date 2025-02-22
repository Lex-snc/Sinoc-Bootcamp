def the_palindrome(text):
    return text [::-1]

text = input("Enter text:")

palindrome = the_palindrome(text)

if (text == palindrome):
    print(palindrome, "is a palindrome")
else:
    print( palindrome, "is not a palindrome")