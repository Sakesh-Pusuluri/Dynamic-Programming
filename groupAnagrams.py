class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = collections.defaultdict(list)
        for word in strs:
            result[tuple(sorted(word))].append(word)
        return result.values()
      

      
      
