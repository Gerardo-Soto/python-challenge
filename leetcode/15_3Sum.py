# Sol YT::: time:10s  Solutions:16,258  Operations:4,458,579

class Solution:
    def threeSum(self, nums):

        nums_sorted = sorted(nums)
        solution = list()
        operations = 0
        solutions = 0   
        for i, a in enumerate(nums_sorted):
            if a == nums_sorted[i-1]:
                #print("Same: a={}, nums_sorted[{}]={}".format(a,i-1,nums_sorted[i-1]))
                continue
            
            l, r = i+1, len(nums_sorted)-1
            while l < r:
                threeSum = a + nums_sorted[l] + nums_sorted[r]

                """OPERACCIONES HECHAS:"""
                operations += 1

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    solution.append([a, nums_sorted[l], nums_sorted[r]])
                    #print("Sol[{}]: [{},{},{}]".format(count, a, nums_sorted[l], nums_sorted[r]))
                    l += 1
                    solutions += 1
                    while nums_sorted[l] == nums_sorted[l - 1] and l < r:
                        l += 1
        
        print("Solutions::: {}, Operations::: {}".format(solutions,operations))
        
        return solution
               


op = Solution()
nums = [0,1,1]
sol = op.threeSum(nums)

#print("Sol: {}".format(sol))
