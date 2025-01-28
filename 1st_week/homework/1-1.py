def check_palindrome(word):
    left = 0
    right = -1
    for i in range(len(word) // 2):
        if word[left] != word[right]:
            return False
        else :
            left += 1
            right -= 1
    return True

text = input("문자를 입력하세요:")
print(check_palindrome(text))