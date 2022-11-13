# Accepted in first term in Python(37 ms). Accepted in second term in Java(1 ms).
# Posted in twitter.
# Ubuntu pastebin: https://pastebin.ubuntu.com/p/hBwYQJJtTf/

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        newWord1, newWord2 = "", ""
        for w in word1:
            newWord1 += w
        for w in word2:
            newWord2 += w

        return newWord1.strip() == newWord2.strip()
