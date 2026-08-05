class MedianFinder(object):

    def __init__(self):

        self.small = []
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small,-num) #adding in maxheap

        heapq.heappush(self.large,-heapq.heappop(self.small)) #adding largest to maxheap

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))    

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()