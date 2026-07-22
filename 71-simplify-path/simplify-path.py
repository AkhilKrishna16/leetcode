class Solution:
    def simplifyPath(self, path: str) -> str:
        # we can track the previous actual directories using a stack
        # so basically 'home' or 'foo' or so on
        
        ret = "/"

        path = path.strip().split("/")
        
        s = []

        for p in path:
            if p == "" or p == '.':
                continue

            if s and p == "..":
                s.pop()
            elif p != "..":
                s.append(p)
        
        return "/" + "/".join(s)