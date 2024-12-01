# Define the TrieNode class
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


# Insert words into the Trie
def insert_word(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True


# Check if a prefix is a valid path in the Trie
def is_prefix(root, word):
    node = root
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    return True


# Check if a complete word is in the Trie
def is_word(root, word):
    node = root
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    return node.is_end_of_word


# Define the main function to find words on the Boggle board using Trie
def find_words(boggle, visited, i, j, word, root, result):
    visited[i][j] = True
    word += boggle[i][j]

    # If word is found, add it to the result set
    if is_word(root, word):
        result.add(word)

    # Explore neighbors if current path is a valid prefix
    if is_prefix(root, word):
        for row in range(max(0, i - 1), min(m, i + 2)):
            for col in range(max(0, j - 1), min(n, j + 2)):
                if not visited[row][col]:
                    find_words(boggle, visited, row, col, word, root, result)

    # Backtrack
    visited[i][j] = False


# Initialize the Boggle board and Trie
boggle = [['T', 'Y', 'R', 'S'],
          ['N', 'U', 'A', 'K'],
          ['Z', 'F', 'E', 'O'],
          ['A', 'C', 'B', 'O']]

# Size of the Boggle board
m = 4
n = 4

# Create a Trie and insert words
root = TrieNode()
dictionary = ['RAY', 'APPLE', 'FAKE', 'BOOKS']
for word in dictionary:
    insert_word(root, word)

# Initialize visited matrix and result set
visited = [[False for _ in range(n)] for _ in range(m)]
result = set()

# Search for words starting from each cell
for i in range(m):
    for j in range(n):
        find_words(boggle, visited, i, j, "", root, result)

# Output the found words
for word in result:
    print(word)
