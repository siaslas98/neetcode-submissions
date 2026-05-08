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
        found = False

        def helperSearch(node, start):
            nonlocal found
            if found: return

            for i in range(start, len(word)):
                ch = word[i]

                if ch in node.children:
                    node = node.children[ch]
                    helperSearch(node, i+1)
                
                elif ch == ".":
                    keys = list(node.children.keys())

                    for key in keys:
                        helperSearch(node.children[key], i+1)

                return
            
            if node.end == True:
                found = True
                return
        
        helperSearch(node, 0)
        return found
               
        
