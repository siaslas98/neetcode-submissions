class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        mp = {}
        maxLen = 1

        for num in nums:
            if num in mp:
                continue

            leftBound, rightBound = num, num
            leftExists = False

            if (num - 1) in mp:
                leftExists = True
                leftBound = mp[num-1][0]
                mp[leftBound][1] = rightBound
            if (num + 1) in mp:
                rightBound = mp[num+1][1]
                mp[rightBound][0] = leftBound
                if leftExists:
                    mp[leftBound][1] = rightBound
            
            maxLen = max(maxLen, rightBound - leftBound + 1)
            mp[num] = [leftBound, rightBound]
        
        return maxLen
            

