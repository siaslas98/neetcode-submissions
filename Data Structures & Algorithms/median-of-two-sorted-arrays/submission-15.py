class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A, B = nums1, nums2
        med = (len(A)+len(B)+1)//2
        evn = (len(A) + len(B)) % 2 == 0

        l, r = 0, len(A)

        while l <= r:
            i = (l+r)//2
            j = med - i

            maxLeftA = A[i-1] if i > 0 else float('-inf')
            minRightA = A[i] if i < len(A) else float('inf')
            maxLeftB = B[j-1] if j > 0 else float('-inf')
            minRightB = B[j] if j < len(B) else float('inf')

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if evn:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    return float(max(maxLeftA, maxLeftB))

            elif maxLeftA > minRightB:
                r = i - 1
            
            elif maxLeftB > minRightA:
                l = i + 1
        






