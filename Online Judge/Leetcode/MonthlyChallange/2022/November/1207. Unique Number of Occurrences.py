# Accepted in first term. I couldn't even think it would be accepted.
# Ubuntu pastebin: https://pastebin.ubuntu.com/p/sN2tGGkD3D/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        track = dict()
        data_set = set()
        for val in arr:
            if track.__contains__(val):
                curVal = track[val]+1
            else:
                curVal = 1
            track[val] = curVal
        for val in track:
            data_set.add(track[val])
        return len(data_set) == len(track.values())
