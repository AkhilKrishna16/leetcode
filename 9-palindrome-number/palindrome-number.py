class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        copy_x = x # 10
        final_x = 0

        while copy_x != 0:
            digit = copy_x % 10 
            final_x = final_x * 10 + digit

            copy_x = copy_x // 10

        return x == final_x