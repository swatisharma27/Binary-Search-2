class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first = firstOccurrence(nums, target)
        last = lastOccurrence(nums, target)

        return [first, last]
        
def firstOccurrence(nums: list[int], target: int):
    N = len(nums)
    low = 0
    high = N - 1

    while low <= high:
        mid = low + (high-low)//2
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
        else: # target == mid
            if mid == 0 or nums[mid] != nums[mid-1]:
                return mid
            else:
                high = mid - 1
    return -1
            
def lastOccurrence(nums: list[int], target: int):
    N = len(nums)
    low = 0
    high = N - 1
    while low <= high:
        mid = low + (high-low)//2
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
        else: # target == mid
            if mid == N-1 or nums[mid] != nums[mid+1]:
                return mid
            else:
                low = mid + 1
    return -1
