class Solution:
    def compress(self, chars: List[str]) -> int: 
        # have a running count using some "sliding window" technique
        # run from the beginning till the current character is different
        # in which case, record the running count as the second character and 
        # the recorded character as the first.
        # then move index by 2 
        # if the character length is greater than or equal to 10, then record the character 
        # then 9, then perform count -= 9, character then left over count (you can have a while loop for this)
        # finally, record the number of characters by just having a seperate count for that and then return this count
        #
        # wait, what happens if you have abbb, so then you would overwrite the first b. so in which case, 
        # you must update count to 1, and have a temp first to record the current before you replace 

        run = 1
        mark = 0
        curr = chars[0]

        i = 1

        while i < len(chars):
            if chars[i] == curr:
                run += 1
            else: 
                # store temp
                temp = chars[i]
                chars[mark] = curr
                mark += 1
                if run >= 10:
                    r = str(run)
                    while len(r) >= 1:
                        chars[mark] = r[0]
                        mark += 1
                        r = r[1:]
                elif run > 1:
                    chars[mark] = str(run)
                    mark += 1
                run = 1
                curr = temp
            i += 1
        
        if curr: 
            chars[mark] = curr
            mark += 1
            if run >= 10:
                r = str(run)
                while len(r) >= 1:
                    chars[mark] = r[0]
                    mark += 1
                    r = r[1:]
            elif run > 1:
                chars[mark] = str(run)
                mark += 1
        return mark
                
