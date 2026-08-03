class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        N = n + m 
        leftLength = (N + 1) // 2

        left, right = 0, min(n, m)
        listA = nums1 if n <= m else nums2
        listB = nums2 if n <= m else nums1

        while left <= right:
            i = (left + right) // 2
            j = leftLength - i

            ALeft = listA[i-1] if i-1 >= 0 else float("-inf")
            ARight = listA[i] if i < min(n, m) else float("inf")
            BLeft = listB[j-1] if j-1 >= 0 else float("-inf")
            BRight = listB[j] if j < max(n, m) else float("inf")

            if ALeft <= BRight and BLeft <= ARight:
                if N % 2 == 0:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
                else:
                    return float(max(ALeft, BLeft))
            elif ALeft > BRight:
                right = i - 1
            elif BLeft > ARight:
                left = i + 1
        

            

        



