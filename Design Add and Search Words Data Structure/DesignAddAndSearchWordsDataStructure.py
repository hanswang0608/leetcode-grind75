class TrieNode:

    def __init__(self, val='', isWord=False):
        self.val = val
        self.isWord = isWord
        self.next = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.next:
                cur.next[word[i]] = TrieNode(word[i], False)
            cur = cur.next[word[i]]
        cur.isWord = True

    def search(self, word: str) -> bool:
        def dfs(root, w):
            if not w:
                return root.isWord
            if w[0] not in root.next and w[0] != '.':
                return False
            if w[0] == '.':
                for n in root.next:
                    if dfs(root.next[n], w[1:]):
                        return True
            else:
                return dfs(root.next[w[0]], w[1:])
            return False
        return dfs(self.root, word)

    def print(self):
        def helper(root):
            print(root.val, root.isWord)
            for n in root.next:
                helper(root.next[n])
        helper(self.root)

wd = WordDictionary()
wd.addWord('bad')
# wd.addWord('dad')
# wd.addWord('mad')
wd.addWord('pp')
wd.print()
print(wd.search('bad'))
# print(wd.search('pad'))
# print(wd.search('.ad'))
print(wd.search('b.'))