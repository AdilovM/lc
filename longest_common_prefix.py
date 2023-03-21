def longest_common_prefix(strs):
  prefix = strs[0]
  i = 0
  while i < len(strs):
    if prefix == strs[i][:len(prefix)]:
      print(prefix)
      i += 1
    else:
      prefix = prefix[:-1]
      i = 0
  return prefix
print(longest_common_prefix(["flower","flow","flight", "flootersk"]))



# print(shortest_string(["flower","flow","flight"]))

# ALPHABET_SIZE = 26
# indexs = 0
# class TrieNode:
#     # constructor
#     def __init__(self):
#         self.isLeaf = False
#         self.children = [None]*ALPHABET_SIZE

# # Function to facilitate insertion in Trie
# # If not present, insert the node in the Trie
# def insert(key, root):
#     pCrawl = root
#     for level in range(len(key)):
#         index = ord(key[level]) - ord('a')
#         if pCrawl.children[index] == None:
#             pCrawl.children[index] = TrieNode()
#         pCrawl = pCrawl.children[index]
#     pCrawl.isLeaf = True

# # Function to construct Trie
# def constructTrie(arr, n, root):
#     for i in range(n):
#         insert(arr[i], root)

# # Counts and returns number of children of the node
# def countChildren(node):
#     count = 0
#     for i in range(ALPHABET_SIZE):
#         if node.children[i] != None:
#             count +=1
#             # Keeping track of diversion in the trie
#             global indexs
#             indexs = i
#     return count

# # Perform walk on trie and return longest common prefix
# def walkTrie(root):
#     pCrawl = root
#     prefix = ""
#     while(countChildren(pCrawl) == 1 and pCrawl.isLeaf == False):
#         pCrawl = pCrawl.children[indexs]
#         prefix += chr(97 + indexs)
#     return prefix or -1

# # Function that returns longest common prefix
# def commonPrefix(arr, n, root):
#     constructTrie(arr, n, root)
#     return walkTrie(root)


# print(commonPrefix(["flower","flow","flight", "flootersk","f"],len(["flower","flow","flight", "flootersk","f"]), TrieNode()))
