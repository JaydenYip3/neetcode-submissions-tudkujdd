class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def dfs(self,node,  board, i, j, seen: set, word: str, res) -> str | None:
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            return 
        if (i,j) in seen:
            return
        DIRECTIONS = [[1,0],[-1,0],[0,1],[0,-1]]
        cur = node.children[ord(board[i][j]) - ord("a")]

        if not cur:
            return

        word += board[i][j]
        seen.add((i,j))

        if cur.endOfWord:
            res.append(word)
            cur.endOfWord = False

        for di, dj in DIRECTIONS:
            self.dfs(cur, board,i + di,j + dj,seen, word, res)  
        seen.remove((i,j))
        return 

    
    def insert(self, word):
        cur = self.root
        for char in word:
            c = ord(char) - ord("a")
            if not cur.children[c]:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True


        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        for word in words:
            self.insert(word) 
        
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                w = self.dfs(self.root, board, i, j, set(), "", res)
                if w:
                    res.append(w)
        return res