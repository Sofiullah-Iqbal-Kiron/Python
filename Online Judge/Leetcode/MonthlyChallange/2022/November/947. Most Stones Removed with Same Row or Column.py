class Solution(object):
    def removeStones(self, stones):
        eliminated = dict()
        for i in range(0, len(stones), 1):
            cur_list = stones[i]
            for j in range(0, len(stones), 1):
                if (not i == j) and (cur_list[0] == stones[j][0] or cur_list[1] == stones[j][1]):
                    if eliminated.__contains__(tuple(cur_list)):
                        if eliminated[tuple(cur_list)] == tuple(stones[j]):
                            pass
                        else:
                            eliminated[tuple(stones[j])] = tuple(cur_list)
                    else:
                        eliminated[tuple(stones[j])] = tuple(cur_list)
        print(eliminated)
        return len(eliminated)
