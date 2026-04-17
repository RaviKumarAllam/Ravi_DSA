class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_distance = n 
        for index, word in enumerate(words):
            if word == target:
                direct_distance = abs(index - startIndex)
              
                wrap_distance = n - direct_distance
              
                min_distance = min(min_distance, direct_distance, wrap_distance)
      
        return -1 if min_distance == n else min_distance
  