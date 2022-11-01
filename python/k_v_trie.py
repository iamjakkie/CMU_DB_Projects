class TrieNode:
    def __init__(self, key_char: str):
        self.key_char = key_char
        self._is_end = False
        self._children = {}

    def hasChild(self, key_char: str):
        return key_char in self._children

    def hasChildren(self):
        return self._children.values()

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

    def __repr__(self):
        return f"TrieNode, key:{self.getKeyChar()}, children: {self.hasChildren()}"


class TrieNodeWithValue(TrieNode):
    def __init__(self, val, tn: TrieNode = None, key_char: str = None):
        if tn is None and key_char:
            tn = TrieNode(key_char)
        self.trieNode = tn
        tn.setEndNode(True)
        self.value = val
        self._is_end = True

    def getValue(self):
        return self.value

    def __repr__(self):
        return f"TrieNodeWithValue, key: {self.trieNode.getKeyChar()}, value: {self.getValue()}, children: {self.trieNode.hasChildren()}"


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
                prev = node
            else:
                prev.insertChildNode(char, TrieNodeWithValue(key_char=char, val=val))

    # def __repr__(self):
    def depth_first_scan(self):
        out = []
        for node in self._root.hasChildren():
            out.append(get_node_char(node))
        return out

    def __repr__(self):
        return self._root.__repr__()


def get_node_char(tn: TrieNode):
    if tn.isEndNode() or isinstance(tn, TrieNodeWithValue):
        return tn.getKeyChar()
    else:
        return tn.getKeyChar()


def main():
    trie = Trie()
    trie.insert("test", "val")
    trie.insert("testosteron", "dupa")
    print(trie)


if __name__ == '__main__':
    main()
