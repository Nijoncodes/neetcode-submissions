class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        """
        Top K freuqent elements is essentially counting the 
        numbers with the most occurances in the list 
        for example, if [1,2,2,2,2,6,6,6,6,3,3,3]
        we esentially have to count how many times the 2 appears 
        the one appears and the 6 appears and the 3. 
        """
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
        sorted_nums = sorted(count.items(), key=lambda x: x[1], reverse=True)

        return [num[0] for num in sorted_nums[:k]]
