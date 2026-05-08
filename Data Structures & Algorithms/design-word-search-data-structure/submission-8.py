import random 

class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
                continue
            if c == "." and len(node.children) > 0:
                node = node.children[list(node.children.keys())[0]]
                continue

            return False
        
        return node.end 
            
            
        
