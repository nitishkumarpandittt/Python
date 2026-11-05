# implement tries methods:
# insert -> apple
# search -> apple
# startswith -> app

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     # insert
#     # TC -> O(L)
#     def insert(self, word):
#         node = self.root
#         for char in word:  # a, p, p, l, e
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_end = True

#     # search exact word
#     # TC -> O(L) -> average length
#     # SC -> O(L*N) -> average lenght * number of words
#     def search(self, word):
#         node = self.root
#         for char in word: # a, p, p, l, e
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return node.is_end

#     # starts with (search for prefix)
#     # TC -> O(L)
#     def startsWith(self, prefix):
#         node = self.root
#         for char in prefix:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return True

# t = Trie()
# t.insert("apple")
# t.insert("apps")
# t.insert("ap")

# print(t.search("apple"))
# print(t.search("a"))

# print(t.startsWith("app"))
# print(t.startsWith("b"))


# implement tries 2


class TrieNode2:
    def __init__(self):
        self.children = {}
        self.endsWith = 0
        self.countPrefix = 0


class Trie2:

    def __init__(self):
        self.root = TrieNode2()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode2
            node = node.children[char]
            node.countPrefix += 1
        node.endsWith += 1

    def countWordsEqualTo(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.endsWith

    def countPrefix(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.countPrefix

    def erase(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                return
            node = node.children[char]
            node.countPrefix -= 1
        node.endsWith -= 1
