class TrieNode:
    def __init__(self, key_char):
        self.key_char = key_char
        self._is_end = False
        self._children = {}

    def hasChild(self, key_char):
        return key_char in self._children

    def hasChildren(self):
        return self._children

    def isEndNode(self):
        return self._is_end

    def getKeyChar(self):
        return self.key_char