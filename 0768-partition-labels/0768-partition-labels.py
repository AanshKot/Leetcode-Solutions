class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        lastIndexHash = {}

        #store the lastIndex of the occurring char
        for i in range(len(s)):
            lastIndexHash[s[i]] = i

        res = []
        partitionSize = 0
        end = 0

        for i, c in enumerate(s):
            partitionSize += 1
            #whenever we read in a last char thats greater than our current partition end (meaning a char occurs further out than our current partition end) increase the partition end
            end = max(end, lastIndexHash[c])

            #if i reaches the end of the partition reset the size back to 0
            if i == end:
                res.append(partitionSize)
                partitionSize = 0

        return res
        