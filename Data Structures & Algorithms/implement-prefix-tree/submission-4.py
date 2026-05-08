class TrieNode:
    def __init__(self):
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if word[0] not in self.root.children:
            self.root.children[word[0]] = TrieNode() # ex mapping: 'a' -> child TrieNode
        curNode = self.root.children[word[0]]

        for i in range(1, len(word)):
            if word[i] not in curNode.children:
                newNode = TrieNode()
                curNode.children[word[i]] = newNode
                curNode = newNode
            else:
                curNode = curNode.children[word[i]]

        curNode.children["*"] = TrieNode()

    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c in node.children:
                node = node.children[c]
                continue
            return False
        return True if "*" in node.children else False

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for c in prefix:
            if c in node.children:
                node = node.children[c]
                continue
            return False

        return True if len(node.children) >= 1 else False
        
        