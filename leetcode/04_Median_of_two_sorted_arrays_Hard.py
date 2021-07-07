class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lenght_1 = len(nums1)
        lenght_2 = len(nums2)
        lenght_nums = len(nums1) + len(nums2)
        media = int(lenght_nums / 2) + 1	# 7 = 3

        aux_1 = 0
        aux_2 = 0

        print(range(media))
        for i in range(media): # 0, 1, [2], (3), 4, 5, 6
            print(f'sprin::{i}')
            if nums1[aux_1] <= nums2[aux_2]:
                if aux_1 == lenght_1 - 1:

                    aux_2 += 1
                    median = nums2[aux_2]
                    
                    print(f'a {nums2[aux_2]} : m:{median}')
                else:
                    
                    aux_1 += 1
                    median = nums1[aux_1]
                    
                    print(f'b {nums1[aux_1]} : m:{median}')

            else:
                if aux_1 == lenght_1 - 1:
                    

                    aux_2 += 1
                    median = nums2[aux_2]
                    
                    print(f'c {nums2[aux_2]} : m:{median}')
                else:
                    aux_1 += 1
                    median = nums1[aux_1]
                    print(f'd {nums1[aux_1]} : m:{median}')
        

#        if lenght_nums%2 == 0:
#            return x

        return median

if __name__ == '__main__':
    nums2 = [1,2]
    nums1 = [7,8,9,10,11,]
    median = Solution()
    print(median.findMedianSortedArrays(nums1,nums2))
