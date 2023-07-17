"""

Given an array of integers, find the length of the longest increasing subsequence.

Write a function length_of_lis(nums) that takes in an array of integers nums and returns
an integer representing the length of the longest increasing subsequence in the array.

Input:
The function length_of_lis takes in a single parameter:

nums (1 <= len(nums) <= 1000): An array of integers where each element represents a number in the sequence.
Output:
The function should return a single output:

An integer representing the length of the longest increasing subsequence in the given array.


Examples:

Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4

Input: nums = [0, 1, 0, 3, 2, 3]
Output: 4

Input: nums = [7, 7, 7, 7, 7, 7, 7]
Output: 1

Input: nums = [1, 3, 2, 5, 4]
Output: 3

"""

def length_of_lis(nums: List[int]) -> int:

        "Write your logic here."

