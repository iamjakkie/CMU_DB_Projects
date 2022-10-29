class TrieNode:
    def __init__(self, key_char:str):
        self.key_char = key_char
        self._is_end = False
        self._children = {}

    def hasChild(self, key_char:str):
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
    def __init__(self, val, tn: TrieNode=None, key_char:str=None):
        if tn is None and key_char:
            tn = super.__init__(key_char)
        self.trieNode = tn
        self.value = val
        self._is_end = True

    def getValue(self):
        return self.value

