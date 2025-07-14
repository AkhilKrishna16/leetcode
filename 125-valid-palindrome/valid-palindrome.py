class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we have a pointer at the front and the back 
        # we use a while loop to move the pointer on each iteration based on the value 

        start, end = 0, len(s) - 1
        s = s.upper()

        while(start < end):
            while not s[start].isalnum() and start < end:
                start += 1
            while not s[end].isalnum() and start < end:
                end -= 1

            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1

            
            
        return True