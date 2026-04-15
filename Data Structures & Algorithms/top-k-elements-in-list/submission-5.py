class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = [[] for _ in range(len(nums) + 1)]

        collection_dict = defaultdict(int)

        for num in nums:
            collection_dict[num] = collection_dict.get(num, 0) + 1

        for key,v in collection_dict.items():
            frequency[v].append(key)

        result = []
        
        for i in range(len(frequency) - 1, 0, -1):
            for freq in frequency[i]:
                result.append(freq)
                if len(result) == k:
                    return result
        return result


            


        
