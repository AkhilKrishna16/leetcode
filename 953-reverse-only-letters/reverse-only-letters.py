class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s) - 1

        c = list(s)

        while left < len(c) and left < right:
            while not c[left].isalpha() and left < right:
                print(f"{left}, {right}")
                left += 1
            while not c[right].isalpha() and right > left:
                print(f"{left}, {right}")
                right -= 1
            
            c[left], c[right] = c[right], c[left]
            left += 1
            right -= 1
        
        return "".join(c)