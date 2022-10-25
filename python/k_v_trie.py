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