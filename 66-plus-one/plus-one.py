class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if simple add digits, just simply increment
        # if have to increment previous counter, check if there is a previous counter
        # if run out of spaces, insert function to beginning with one 

        if not digits:
            return [1]

        digits[-1] += 1

        if digits[-1] < 10:
            return digits
        else:
            i = 1
            while digits[-i] >= 10:
                digits[-i] = 0
                if abs(-i - 1) <= len(digits):
                    digits[-i - 1] += 1
                else:
                    digits.insert(0, 1)
                    break

                i += 1
        return digits