class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        if bills[0] != 5:
            return False

        # fifo

        # add to the list in the specified order
        # 5->5->5->10->20
        # if 5 continue
        # if 10, keep track of the amount of 5's we have. if we have one, keep going because we have enough
        # if anything other than a 5, just divide and see how much you can possibly get. if you have enough, subtract and continue, otherwise return

        
        # if 5, add
        # if 10, see if we have a 5
        # if 20, see if we have 3 5's or 1 10 and 2 5's

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives >= 1:
                    fives -= 1
                    tens += 1
                else:
                    return False
            else:
                if fives >= 1 and tens >= 1:
                    fives -= 1
                    tens -= 1
                elif fives >= 3:
                   fives -= 3
                else:
                    return False
                

        return True