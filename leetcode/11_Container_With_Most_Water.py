"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
"""

class Solution:
	def maxArea(self, height):
		end = len(height) - 1
		output = 0
		start = 0
		while (start < end):
			distance = end - start
			if height[start] <= height[end]:
				contain = distance * height[start]
				print("+> area: d:{} * h:{} = {}".format(distance, height[start], contain))
				start += 1
            
			else:
				contain = distance * height[end]
				print("<- area: d:{} * h:{} = {}".format(distance, height[start], contain))
				end -= 1

			if contain > output:
				output = contain
            
		return output

s = Solution()
v =[1,8,6,2,5,4,8,3,7]
print(s.maxArea(v))


"""
Runtime: 652 ms, faster than 93.83% of Python3 online submissions for Container With Most Water.
Memory Usage: 27.6 MB, less than 50.99% of Python3 online submissions for Container With Most Water.
"""

