class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
      
        # Counter to track frequency of elements seen so far in array A
        frequency_a = Counter()
      
        # Counter to track frequency of elements seen so far in array B
        frequency_b = Counter()
      
        # Process both arrays element by element
        for element_a, element_b in zip(A, B):
            # Update the frequency counters for current elements
            frequency_a[element_a] += 1
            frequency_b[element_b] += 1
          
            # Count common elements by taking minimum frequency for each element
            # that appears in array A's prefix
            common_count = sum(
                min(freq_in_a, frequency_b[element]) 
                for element, freq_in_a in frequency_a.items()
            )
            result.append(common_count)
      
        return result