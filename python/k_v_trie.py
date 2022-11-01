class TrieNode:
    def __init__(self, key_char: str):
        self.key_char = key_char
        self._is_end = False
        self._children = {}

    def hasChild(self, key_char: str):
        return key_char in self._children

    def hasChildren(self):
        return self._children

    def isEndNode(self):
        return self._is_end

    def getKeyChar(self):
        return self.key_char

    def insertChildNode(self, key_char: str, child):
        if not self.hasChild(key_char):
            self._children[key_char] = child

    def getChildNode(self, key_char):
        if key_char in self._children:
            return self._children[key_char]

    def removeChildNode(self, key_char):
        if key_char in self._children:
            del self._children[key_char]

    def setEndNode(self, is_end: bool):
        self._is_end = is_end


class TrieNodeWithValue(TrieNode):
    def __init__(self, val, tn: TrieNode = None, key_char: str = None):
        if tn is None and key_char:
            tn = super().__init__(key_char)
        self.trieNode = tn
        self.value = val
        self._is_end = True

    def getValue(self):
        return self.value


class Trie:
    def __init__(self):
        self._root = TrieNode("\0")
        self._latch = None
        self._keys = set()

    def insert(self, key: str, val):
        if not key:
            return False
        if key in self._keys:
            return False
        key_len = len(key) - 1
        prev = self._root
        for i, char in enumerate(key):
            if i < key_len:
                node = TrieNode(char)
                prev.insertChildNode(char, node)
                last = node
                prev = node
            else:
                prev.insertChildNode(char, TrieNodeWithValue(tn=last, key_char=char, val=val))

    # def __repr__(self):


def main():
    trie = Trie()
    trie.insert("test", "val")
    print(trie._root._children)
    node = trie._root
    while node:
        print(node)
        node = node.getChildNode()


if __name__ == '__main__':
    main()
