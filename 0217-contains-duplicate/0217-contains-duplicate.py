class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        data = {}

        for num in nums:
            if num in data and data[num]>=1:
                return True
            data[num]=data.get(num,0)+1
        
        return False