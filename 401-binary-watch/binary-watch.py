class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn < 0 or turnedOn > 10:
            return []
        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    if m < 10:
                        res.append(f"{h}:0{m}")
                    else:
                        res.append(f"{h}:{m}")
                        
        return res