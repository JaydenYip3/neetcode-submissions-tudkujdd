class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suf = []

        prefix = 1
        suffix = 1
        
        for num in nums:
            pre.append(prefix)
            prefix = prefix * num
        for num in nums[::-1]:
            suf.append(suffix)
            suffix = suffix * num
        suf.reverse() 
        result = []

        for i in range(len(nums)):
            result.append(pre[i] * suf[i])
        
        return result
                
