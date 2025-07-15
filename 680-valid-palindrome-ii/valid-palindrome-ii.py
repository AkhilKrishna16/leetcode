class Solution:
    def validPalindrome(self, s: str) -> bool:
       # start a pointer at 0 and len(s) - 1
       # move the pointers towards each other
       # when ever the two characters dont equal each other, move the left pointer + 1
       # and mark k = k - 1
       # if not equal characters happen again and k = 0, then return false
        def check_palindrome(s):
            start, end = 0, len(s) - 1
            while start < end:
                if s[start] != s[end]:
                    return False
                else:
                    start += 1
                    end -= 1
            return True

        start, end = 0, len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return check_palindrome(s[start + 1: end + 1]) or check_palindrome(s[start:end])
                # only way is to check both ways
            else:
                start += 1
                end -= 1

        return True