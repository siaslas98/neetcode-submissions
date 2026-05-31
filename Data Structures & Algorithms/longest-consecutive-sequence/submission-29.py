class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_mapper = {}
        max_length = 1

        for i in range(len(nums)):
            if nums[i] in num_mapper:
                continue
            
            leftBound = rightBound = None
            curNum, prevNum, nextNum = nums[i], nums[i] - 1, nums[i] + 1
            
            if prevNum in num_mapper:
                leftBound = num_mapper[prevNum][0]
                if nextNum in num_mapper:
                    rightBound = curNum + num_mapper[nextNum][1]

                    num_mapper[curNum] = [leftBound, None] # Set current number info
                    num_mapper[rightBound][0] = leftBound # Update right bound root info
                    num_mapper[leftBound][1] += (1 + num_mapper[nextNum][1]) # Update left bound size info
                else:
                    num_mapper[curNum] = [leftBound, None]
                    num_mapper[leftBound][1] += 1
            
            elif nextNum in num_mapper:
                num_mapper[curNum] = [curNum, 1 + num_mapper[nextNum][1]]
                rightBound = curNum + num_mapper[nextNum][1]
                num_mapper[rightBound][0] = curNum
            
            else:
                num_mapper[curNum] = [curNum, 1]
                continue
            
            if leftBound is not None:
                max_length = max(max_length, num_mapper[leftBound][1])
            else:
                max_length = max(max_length, num_mapper[curNum][1])

        
        return max_length

            