"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Datos
Tema:LeetCode
Programa:42. Trapping Rain Water.
Creador:Soto Alvarez del Castillo Gerardo Alvarez.
Correo:gerardo.8.soto@gmail.com
Compilacion:(Liux) python3.7 file.py 
Version:1.0
Fecha:02-Jul-21  22:11
Observaciones:

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        len_height = len(height)
        water = 0
        current_top_level = 0
#        left_top = height[0]
        left_index = 1
#        right_top = height[len_height]
        right_index = len_height - 2

        for bar in range(len_height - 2):
            if height[left_index] > height[right_index]:
                current_top_level = height[right_index]
                if height[right_index] > height[right_index - 1]:
                    water += ( height[right_index] - height[right_index - 1])

                right_index -= 1

            else:
                current_top_level = height[left_index]
                if height[left_index] > height[left_index + 1]:
                    water += ( height[left_index] - height[left_index + 1])

                left_index += 1

        return water


"""
Runtime: 48 ms, faster than 92.74% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 14.8 MB, less than 64.34% of Python3 online submissions for Trapping Rain Water.
"""