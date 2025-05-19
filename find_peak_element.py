class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        N = len(nums)

        low = 0
        high = N - 1

        while low <= high:
            mid = low + (high-low)//2
            # mid == 0, no left side ; mid == N-1, no right side
            if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == N-1 or nums[mid] > nums[mid+1]): 
                return mid
            else:
                if mid != 0 and nums[mid] < nums[mid-1]: # mid != 0 - this is to avoid out of bounds
                    high = mid - 1
                else:
                    low = mid + 1
        return -1
