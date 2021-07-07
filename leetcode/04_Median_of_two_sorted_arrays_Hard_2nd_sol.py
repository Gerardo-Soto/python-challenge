#########pop list

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lenght_nums = (len(nums1) + len(nums2))
        print(f'{len(nums1)}, {len(nums2)}, m:{lenght_nums/2}')
        start = True
        medium_2 = None
        #if lenght_nums%2 == 0 or ( len(nums1) == 0 and len(nums2)%2 == 0 ) or ( len(nums2) == 0 and len(nums1)%2 == 0 ):
        if True:
            print(f'ciclos hacer: {range(int(lenght_nums/2) + 1)}')
            for i in range(int(lenght_nums/2) + 1):
                if len(nums1) != 0 and len(nums2) != 0:
                    if start:
                        if nums1[0] < nums2[0]:
                            medium_1 = nums1.pop(0)
                            
                        else:
                            medium_1 = nums2.pop(0)
                            
                        start = False

                    else:
                        if nums1[0]  <= nums2[0]:
                            medium_2 = medium_1
                            medium_1 = nums1.pop(0)
                        elif nums1[0] >= nums2[0]:
                            medium_2 = medium_1
                            medium_1 = nums2.pop(0)
                else:
                    #print(f'{len(nums1)}, {len(nums2)}')
                    if len(nums1) == 0:
                        if start:
                            medium_1 = nums2.pop(0)
                            start = False
                        else:
                            medium_2 = medium_1
                            medium_1 = nums2.pop(0)

                    else:
                        if start:
                            medium_1 = nums1.pop(0)
                            start = False
                        else:
                            medium_2 = medium_1
                            medium_1 = nums1.pop(0)
                
                print(f'ciclo: {i}, medium_1:{medium_1}, medium_2:{medium_2}')
            
            if lenght_nums%2 != 0:
                print(f'(IMPAR)Medium:: {medium_1}')
            else:
                solve = (medium_1 + medium_2) / 2
                print(f'(PAR)Medium:: {solve}')
        

if __name__ == '__main__':
    s = Solution()
    n=[1,2]
    a=[3,4]
    s.findMedianSortedArrays(n,a)

"""
SUCCESS

Runtime:    80 ms, faster than  49.01%  of Python online submissions for Median of Two Sorted Arrays.

Memory usage:   13.7 MB, less than 52.37% of Python online submissions for Median of two Sorted Arrays.
"""
