""" Matrix  Diagonal Sum"""

""" Given a square mattrix 'mat', return the sum of the  matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secundary diagonal that are not part of the primary diagonal.
"""

class Solution:
    def diagonalSum(self, mat):
        #print(type(mat))
        #print(dir(mat))
        for row in mat:
            print(row)

        n = len(mat)
        print("Len(mat): {}".format(n))
        #print(mat)
        if (n % 2) == 0:
            print("par")
            flag_left = 0
            flag_right = n-1
            diagonal_sum = 0
            for row in mat:
                #print("n: %2 {}".format(n % 2))
                diagonal_sum += int(row[flag_left])
                diagonal_sum += int(row[flag_right])
                flag_left += 1
                flag_right -=1
                
        else:
            print("impar")
            flag_left = 0
            flag_right = n-1
            flag_middle = int(n/2)
            diagonal_sum = 0
            for row in mat:
                diagonal_sum += int(row[flag_left])
                diagonal_sum += int(row[flag_right])
                if flag_left == flag_middle:
                    diagonal_sum -= row[flag_middle]
                
                flag_left += 1
                flag_right -= 1

        return diagonal_sum


def run():
    mat = [[1,2,3],
           [4,5,6],
           [7,8,9]]
    diagonal_matrix = Solution()
    sol = diagonal_matrix.diagonalSum(mat)
    print("Sol: {}".format(sol))

if __name__ == '__main__':
    run()


"""Result:
Success     DEtails:

Runtime:    148 ms, faster than 5.93% of Python online submissions for Matrix Diagonal Sum.

Memory usege: 13.7 MB, less than 16.85% of Python online submissions for Matrix Diagonal Sum.
"""
