from typing import List
from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:
    
      
        def find_root(index: int) -> int:
            if parent[index] != index:
                # Path compression: directly connect to root
                parent[index] = find_root(parent[index])
            return parent[index]
      
        # Initialize Union-Find structure
        array_length = len(source)
        parent = list(range(array_length))  
        for index_a, index_b in allowedSwaps:
            parent[find_root(index_a)] = find_root(index_b)
        component_value_counts = defaultdict(Counter)
        for index, value in enumerate(source):
            root = find_root(index)
            component_value_counts[root][value] += 1
      
        hamming_distance = 0
        for index, value in enumerate(target):
            root = find_root(index)
            component_value_counts[root][value] -= 1
            if component_value_counts[root][value] < 0:
                hamming_distance += 1
      
        return hamming_distance