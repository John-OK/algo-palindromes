def palindrome(word):
    validChars = "abcdefghijklmnopqrstuvwxyz0123456789"
    validStr = ""

    for char in str(word).lower():
        if char in validChars:
            validStr += char
    
    midpoint = int(len(validStr) / 2)

    word_front_half = validStr[:midpoint]
    word_back_half_reversed = validStr[-1:-(midpoint) - 1:-1]

    if word_front_half == word_back_half_reversed:
        return True
    return False