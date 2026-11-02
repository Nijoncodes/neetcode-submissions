class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """"
        BRUTAL FORCE SOLUTION 

        groups = [] start with empty array 

        for word in strs: # Nested for loops: (on)2 run time 
            for groups in groups:
                if sorted(word) == sorted(group[0]):
                    group.append(word)
                    break
            
            if found == False:
                groups.append([word])
        
    
        return groups 

        """
        # Efficent solution

        groups = {}

        for word in strs:
            
            key = "".join(sorted(word))

            if key not in groups:

                groups[key] = []

            groups[key].append(word)
        
        return list(groups.values())

    
