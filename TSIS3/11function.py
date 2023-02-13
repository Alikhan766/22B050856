def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if string[left_pos] != string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True


str0 = 'level'
str1 = 'palindrome'
str2 = 'aaaa'
str3 = 'Never odd or even'

print(isPalindrome(str0))
print(isPalindrome(str1))
print(isPalindrome(str2))
print(isPalindrome(str3))
