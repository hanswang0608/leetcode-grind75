class Trie:
    class Node:
        def __init__(self, val = ''):
            self.val = val
            self.children = {}
            self.isInserted = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        def insertHelper(root, wordSoFar, wordRemainder):
            if not wordRemainder:
                root.isInserted = True
                return
            prefix = wordSoFar + wordRemainder[0]
            if wordRemainder[0] not in root.children:
                root.children[wordRemainder[0]] = self.Node(prefix)
            insertHelper(root.children[wordRemainder[0]], prefix, wordRemainder[1:])

        insertHelper(self.root, '', word)

    def search(self, word: str) -> bool:
        def searchHelper(root, word):
            if not root:
                return False
            if not word:
                return True if root.isInserted else False
            if word[0] in root.children:
                return searchHelper(root.children[word[0]], word[1:])
            else:
                return False
        
        return searchHelper(self.root, word)
        
    def startsWith(self, prefix: str) -> bool:
        def startsWithHelper(root, prefix):
            if not root:
                return False
            if not prefix:
                return True
            if prefix[0] in root.children:
                return startsWithHelper(root.children[prefix[0]], prefix[1:])
            else:
                return False
        
        return startsWithHelper(self.root, prefix)
    
    def print(self):
        def printHelper(root):
            if not root:
                return
            print(root.val)
            for child in root.children:
                printHelper(root.children[child])
                
        printHelper(self.root)

    def printLeaves(self):
        def printHelper(root):
            if not root:
                return
            if root.isInserted:
                print(root.val)
            for child in root.children:
                printHelper(root.children[child])

        printHelper(self.root)



# Your Trie object will be instantiated and called as such:
trie = Trie()
print(trie.insert("aaa"))
print(trie.insert("aa"))
print(trie.search('aaa'))
trie.printLeaves()