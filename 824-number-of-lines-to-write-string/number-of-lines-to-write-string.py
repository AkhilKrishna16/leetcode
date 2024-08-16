class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        current_width = 0
        i = 0

        while i < len(s):
            width = widths[ord(s[i]) - 97]
            if current_width + width > 100:
                current_width = width
                lines += 1
            else:
                current_width += width

            i += 1
        
        return [lines, current_width]