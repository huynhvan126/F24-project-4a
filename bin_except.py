# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 10/23/2024
# Description: Modify binary search from the exploration.
class TargetNotFound(Exception):
    """
    Exception raised when a target is not found.
    """
    pass

def bin_except(arr, target):
    """
    Performs binary search on a sorted list and raises TargetNotFound exception if target is not found.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    raise TargetNotFound(f"Target {target} not found in the list.")