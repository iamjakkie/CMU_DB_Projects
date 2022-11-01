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
        tn._is_end = True
        self.value = val
        self._is_end = True

    def getValue(self):
        return self.value

    def __repr__(self):
        return f"TrieNodeWithValue, key: {self.trieNode.getKeyChar()}"


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
            print(char)
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
            print(node)
            out.append(get_node_char(node))
        return out


def get_node_char(tn: TrieNode):
    if isinstance(tn, TrieNodeWithValue):
        return tn.trieNode.getKeyChar()
    else:
        for i in tn.hasChildren():
            print(i)
            return get_node_char(i)


def main():
    trie = Trie()
    trie.insert("test", "val")
    print(trie.depth_first_scan())


if __name__ == '__main__':
    main()
