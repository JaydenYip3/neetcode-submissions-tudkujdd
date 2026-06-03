class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = defaultdict(int)

        for i in range(len(nums)): 
            if target - nums[i] in values:
                return [values.get(target - nums[i]), i]
            values[nums[i]] = i

        return []

        