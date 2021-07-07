# Sol YT::: time:10s  Solutions:16,258  Operations:4,458,579
# MOD if [24] ::: time::11s  Sol: =  Op: 3,489,167
# MOD if [24, 28] ::: time:::8s  Sol::: ===  Op:1,680,090

class Solution:
    def threeSum(self, nums):

        nums_sorted = sorted(nums)
        solution = list()
        operations = 0
        solutions = 0   
        rep = 0
        r = len(nums_sorted) - 1
        print("V: {}".format(nums_sorted))
        for i, a in enumerate(nums_sorted):
            if a == nums_sorted[i-1]:
                #print("Same: a={}, nums_sorted[{}]={}".format(a,i-1,nums_sorted[i-1]))
                rep += 1
                if a == 0 and rep == 3 and [0,0,0] not in solution and (a + nums_sorted[i + 1] + nums_sorted[r]) == 0:
                    solution.append([0,0,0])
                    solutions += 1
                    print("1")
                continue
            
            l, r = i+1, len(nums_sorted) - 1
            while l < r:
                threeSum = a + nums_sorted[l] + nums_sorted[r]
                print("Op: {} + {} + {} = {}   | r={}, l={} (r+l)/2={}".format(a,nums_sorted[l],nums_sorted[r],threeSum,r,l,int((r+l)/2)))

                """OPERACCIONES HECHAS:"""
                operations += 1
                if operations > 200:
                    return 0

                if int((r+l)/2) == l:
                    solution_aux = [a, nums_sorted[l], nums_sorted[r]]
                    l += 1 
                    if threeSum == 0 and solution_aux not in solution:
                        solution.append(solution_aux)
                        solutions += 1
                        print("2")
                    continue
                elif threeSum > 0 and nums_sorted[int((r+l)/2)] + a + nums_sorted[l] >= 0:
                    r = int((r+l)/2) 
                elif threeSum > 0:
                    r -= 1
                elif threeSum < 0 and nums_sorted[int((r+l)/2)] + a + nums_sorted[r] <= 0:
                    l = int((r+l)/2) 
                elif threeSum < 0:
                    l += 1
                else:
                    solution_aux = [a, nums_sorted[l], nums_sorted[r]]
                    if solution_aux not in solution:
                        solution.append(solution_aux)
                        print("3")
                        solutions += 1
                    #print("Sol[{}]: [{},{},{}]".format(count, a, nums_sorted[l], nums_sorted[r]))
                    l += 1
                    while nums_sorted[l] == nums_sorted[l - 1] and l < r:
                        l += 1
        
        print("Solutions::: {}, Operations::: {}".format(solutions,operations))
        
        return solution
               


op = Solution()
#nums=[-1,0,1,2,-1,-4,-2,-3,3,0,4] #oooo
#nums=[-1,0,1,2,-1,-4]
#nums=[4,4,3,-5,0,0,0,-2,3,-5,-5,0]
#nums=[2,2,-1,-3,3,1,-2,1,-2,3,0,-5,0,4,-3,3]
nums=[0,0,0] #oooo
sol = op.threeSum(nums)

print("Sol: {}".format(sol))
