# 时间复杂度O(N)
# 空间复杂度O(1)
# 原地哈希

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:


def main():
    nums = list(map(int, input().split()))
    target = int(input())
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)


if __name__ == "__main__":
    main()