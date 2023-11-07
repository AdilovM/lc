class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    result = {}
    for word in strs:
        letter_count = [0 for _ in  range(26)] #array with length of alphabet
        for letter in word:
            letter_count[ord(letter)-97] += 1
        listhash = ''.join((str(l)+" ") for l in letter_count)
        print(listhash)
        if listhash not in result:
            result[listhash] = []
        result[listhash].append(word)
    return result.values()