from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1      # index to place next valid element
        count = 1
        n = len(nums)

        for i in range(1, n):  # 1 to (n-1)
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2: # overwriting j with i 
                nums[j] = nums[i]
                j += 1

        return j
