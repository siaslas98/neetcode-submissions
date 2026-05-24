class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Traverse the array
        # If nums[i] is found in the hashmap, look at its value
        # If value + 1 is greater than longest, update longest
        if not nums:
            return 0

        num_map = {}
        longest = 0

        for i in range(len(nums)):

            if nums[i] in num_map:
                continue

            left = num_map.get(nums[i]-1, 0)
            right = num_map.get(nums[i]+1, 0)
            total = left + right + 1

            num_map[nums[i]] = total
            num_map[nums[i]-left] = total
            num_map[nums[i]+right] = total

            longest = max(longest, total)

        
        return longest





            
        

