from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = dict()

        for i, num in enumerate(nums):
            v = target - num
            if v in idx:
                return [idx[v], i]
            idx[num] = i

        return []


def main():
    nums = list(map(int, input().split()))
    target = int(input())
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)


if __name__ == "__main__":
    main()
