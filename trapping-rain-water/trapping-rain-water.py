class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        trapped_water = 0
        
        left_idx, right_idx = 0, len(height) - 1
        left_max, right_max = 0, 0
        
        while left_idx < right_idx:
            left_max = max(left_max, height[left_idx])
            right_max = max(right_max, height[right_idx])
            
            if left_max <= right_max:
                trapped_water += left_max - height[left_idx]
                left_idx += 1
            else:
                trapped_water += right_max - height[right_idx]
                right_idx -= 1
        
        return trapped_water