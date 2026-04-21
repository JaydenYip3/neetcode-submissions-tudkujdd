class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
 
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            val = ord(c) - ord("a")
            if cur.children[val] == None:
                cur.children[ord(c) - ord("a")] = TrieNode()
            cur = cur.children[val]
        
        cur.endOfWord = True   

    def search(self, word: str) -> bool: 
        return self.dfs(self.root, word)
        
    def dfs(self, node: TrieNode, word: str) -> bool:
        if not word:
            return node.endOfWord
        
        c = word[0]
        if c == '.':
            for child in node.children:
                if child and self.dfs(child, word[1:]):
                    return True
            return False
        else:
            val = ord(c) - ord("a")
            child = node.children[val]
            if not child:
                return False
            return self.dfs(child , word[1:])

