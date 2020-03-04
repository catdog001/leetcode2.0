''''
太复杂了，没做出来
input: org list[int], seqs list[list]. have order? seq has the same order with Org element.  repeated word in Org? N, in seq list list? No
output: True or False
corner case:
Org is None, is [] -> False
seq is None is [] -> False
Org and seq is None or [] -> True
if org elem != seq elem , False
Org has only one, seq has only one, and same -> True, else False

A.topological sort
Method:
create the indegree [] and outdegree[[]] by org and seqs
use stack to save and  traversal nodes with 0 indegree
use DFS to visit node, save the path node in tmp
when reach to terminal, save tmp in res
compare res element with Org, if Org in res, Return True, Else return False

time complexity O(V + E), space complexity O(V)

'''

class Solution:
    def sequenceReconstruction(self, org, seqs) -> bool:
        if not org and not seqs:  # corner case
            return True
        if not org:
            return False
        if not seqs:
            return False
        if org == seqs[0]:
            return True

        tmp = set()
        for elem in seqs:
            for val in elem:
                tmp.add(val)
        if set(org) != tmp:
            return False

        indegree = [0] * len(org)
        outdegree = [[] for _ in range(len(org))]

        for elem in seqs:
            length = len(elem)
            for i in range(0, length - 1):
                indegree[elem[i + 1]] += 1
                outdegree[elem[i]] = elem[i + 1]

        if indegree.count(0) > 1:
            return False

        stack = indegree.index(0)

        tmp = []
        res = []
        for index in stack:
            self.dfs(index, tmp, res, outdegree, seqs)

        if org in res:
            return True
        else:
            return False

    def dfs(self, index, tmp, res, outdegree, seqs):  # save path in res
        if outdegree[index] == []:
            res.append(tmp[:])
            return

        tmp.append(seqs[index])
        for elem in outdegree[index]:
            self.dfs(elem, tmp, res, outdegree, seqs)
        tmp.pop()
        return

x = Solution()
x.sequenceReconstruction([1,2,3], [[1,2],[1,3]])