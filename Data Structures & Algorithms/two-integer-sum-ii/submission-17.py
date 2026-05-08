class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0

        while i < len(numbers):
            comp = target - numbers[i]
            print(comp)

            l = i + 1
            r = len(numbers) - 1

            while l <= r:
                mid = l + (r-l) // 2

                if numbers[mid] == comp:
                    return [i+1, mid+1]
                
                elif numbers[mid] < comp:
                    l = mid + 1
                
                elif numbers[mid] > comp:
                    r = mid - 1
            i += 1
            
            