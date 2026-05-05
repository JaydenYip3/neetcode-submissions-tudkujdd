class MedianFinder:

    def __init__(self):
        self.length = 0
        self.nums = []  

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()
        self.length += 1
         
    def findMedian(self) -> float:
        if self.length % 2 == 0:
            return (self.nums[self.length // 2 - 1] + self.nums[self.length // 2]) / 2
        else:
            return self.nums[self.length // 2]


        
        