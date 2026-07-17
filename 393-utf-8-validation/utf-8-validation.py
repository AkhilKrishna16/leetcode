class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # process the current byte, then count the number of ones until you find the correct number of zeroes
        # then take the number of ones, and then fast-forward that number of bytes, checking each byte 
        # to make sure that each follow the 10 pattern (which you can do by checking if the value is <= 191 &&)
        # >= 128; finally, if each byte follows, then you just read the current one and call it a day
        # however, if the number of ones you find is zero before you reach the first zero in the current byte,
        # then skip to the next one and read again
        i = 0
        while i < len(data):
            curr = bin(data[i])[2:]
            j = 0
            num_ones = 0
            if len(curr) < 8:
                curr = "0" * (8 - len(curr)) + curr
            
            while j < len(curr) and curr[j] == "1":
                num_ones += 1
                j += 1
            if num_ones > 4 or num_ones == 1:
                return False
            if num_ones == 0:
                i += 1
            else:
                start = i + 1
                end = start + num_ones - 1
                if end > len(data):
                    return False
                for k in range(start, end):
                    if data[k] > 191 or data[k] < 128:
                        return False
                
                i = end
        return True
