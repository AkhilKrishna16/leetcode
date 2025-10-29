class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        def compute_neighbors(word):
            ret = []
            for i in range(len(word)):
                for curr_letter in "abcdefghijklmnopqrstuvwxyz":
                    # replace the character with every possible character
                    if curr_letter != word[i]:
                        new_word = word[:i] + curr_letter + word[i + 1:]
                        if new_word in wordList:
                            ret.append(new_word)
            return ret
        
        q = deque([(beginWord, 1)])
        seen = {beginWord}

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            neighbors = compute_neighbors(word)
            for neighbor in neighbors:
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append((neighbor, steps + 1))
        
        return 0