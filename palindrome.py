# Old code

# def palindrome(word):
#     word = word.replace(' ','')
#     word = word.lower()
#     inverted_word = word[::-1]
#     if word == inverted_word:
#         return True
#     else:
#         return False

# def main():
#     word = input('Please write a word: ')
#     is_palindrome = palindrome(word)
#     if is_palindrome == True:
#         print('It is a palindrome')
#     else:
#         print('It is not a palindrome')


# New code

def is_palindrome(string:str) -> bool:
    string = string.replace("", "").lower()
    return string == string [::-1]

def main():
    print(is_palindrome(100))

if __name__ == '__main__':
    main()