# Ahmad M. Osman - Dr. Kent Lee, CS360

# Dr. Lee, please notice that if multiple words were seperated by nothing but punctuation, like "Happiness.--That", my string manipulation to remove punctuation will transfer it into "happinessthat". I did not want to put more time into cleaning the words as leaving "happinessthat" like it that is helping to test the Bloom Filter.


import math
import string


class Trie:
    def __insert(node, item):
        """# This is the recursive insert function.
        if len(item) == 0:
            return None
        elif node == None:
            print(item[0])
            node = Trie.TrieNode(item[0])
            node.follows = Trie.TrieNode("")
            Trie.__insert(node.follows, item[1:])
        elif item[0] == node.item:
            print('\t' + item[0])
            node.follows = Trie.TrieNode("")
            Trie.__insert(node.follows, item[1:])
        else:
            print('\t\t' + item)
            node.next = Trie.TrieNode(item[1:2])
            Trie.__insert(node.next, item) """

    def __contains(node, item):
        """# This is the recursive membership test.
        pass """
        pass

    class TrieNode:
        def __init__(self, item, next=None, follows=None):
            self.item = item
            self.next = next
            self.follows = follows

    def __init__(self):
        self.start = None

    def insert(self, item):
        self.start = Trie.__insert(self.start, item)

    def __contains__(self, item):
        return Trie.__contains(self.start, item)


def main():
    words = []
    with open("wordsEn.txt") as openfile:
        words = openfile.readlines()

    trie = Trie()
    for word in words:
        word = word.strip()
        word += '$'
        trie.insert(word)


"""     # count = 0
    with open("declaration.txt") as openfile:
        exclude = set(string.punctuation)
        for line in openfile:
            for word in line.split():
                # removing any punctuation
                word = ''.join(ch for ch in word if ch not in exclude)
                # lowering
                word = word.lower()
                if word not in bloom:
                    # count += 1
                    print(word)
    # print(count) """


if __name__ == "__main__":
    main()
