class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        low = 0
        high  = N - 1

        while (low <= high):
            # full array sorted
            if nums[low] <= nums[high]:
                return nums[low]

            mid = low + (high-low)//2
            if mid!= 0 and nums[mid] < nums[mid-1]: # To avoid out of bound when mid = 0, and when arr[mid-1] > arr[mid], i.e., pivot
                return nums[mid]

            elif nums[low] <= nums[mid]: #left sorted - eliminate left, move to right half
                low = mid + 1
            else:
                high = mid - 1 #right sorted - eliminate right, move to left half
        return -1
 