def is_palindrome(given_word):
    palindrome_string = given_word[::-1]
    if given_word.casefold()==palindrome_string.casefold():
        output="given strig is a palindrome"
    else:
        output="given word is not a palindrome"
    
    return output

word = input("Enter the word: ")
result = is_palindrome(word)
print(result)