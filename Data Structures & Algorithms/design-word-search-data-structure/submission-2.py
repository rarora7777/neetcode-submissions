class TrieNode:
    # val: str | None = None
    children: dict[str, TrieNode] = {}

    def __init__(self):
        # self.val = val
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                # print("Inserted", ch)
                node.children[ch] = TrieNode()
            node = node.children[ch]
        
        node.children['|'] = TrieNode()
            
    def search_subtree(self, node: TrieNode, word: str) -> bool:
        # print("Searching for", word)
        for i, ch in enumerate(word):
            if ch != '.':
                if ch in node.children:
                    # print("matched", ch)
                    node = node.children[ch]
                else:
                    return False
            else:
                for key, child in node.children.items():
                    # print("matched . with", key)
                    if self.search_subtree(child, word[i+1:]):
                        return True
                return False
        
        return True


    def search(self, word: str) -> bool:
        return self.search_subtree(self.root, word + '|')
        
