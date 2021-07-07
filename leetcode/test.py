class Solution:
	def trap(self, height ):
		len_height = len(height)
		water = 0
		current_top_level = 0
		left_index = 0
		right_index = len_height - 1
		print("len::: {}".format(len_height))
		while left_index < right_index:
			if height[left_index] > height[right_index]:
				
				if current_top_level < height[right_index]:
					current_top_level = height[right_index]
#				if height[right_index] > height[right_index - 1]:
				else:
					water += ( current_top_level - height[right_index])

				right_index -= 1
			else:
				if current_top_level < height[left_index]:
					current_top_level = height[left_index]

				#if height[left_index] > height[left_index + 1]:
				else:
					water += ( current_top_level - height[left_index])

				left_index += 1

		return water

s = Solution()
op1 = [0,1,0,2,1,0,1,3,2,1,2,1]
op2 = [4,2,0,3,2,5]

print(s.trap(op1))
print(s.trap(op2))

