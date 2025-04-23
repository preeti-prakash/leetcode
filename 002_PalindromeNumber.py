# Given an integer x, return true if x is a palindrome, and false otherwise.

def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        x_length = len(x_str)
        x_reverse= []
        for i in range(x_length-1,-1,-1):
            x_reverse.append(x_str[i])

        for i in range(x_length):
            if x_reverse[i] != x_str[i]:
                return False
        return True

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))