# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
# เขียน Recursive เพื่อหาว่า String ที่รับเข้ามาเป็น Palindrome หรือไม่

# Enter Input : abba
# 'abba' is palindrome


def isPalindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])

inp = input('Enter Input : ')
if isPalindrome(inp):
    print(f"'{inp}' is palindrome")
else:
    print(f"'{inp}' is not palindrome")