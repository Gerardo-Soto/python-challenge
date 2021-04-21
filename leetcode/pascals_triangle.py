class Solution(object):
    def generate(self,numRows):
        """
        :type   numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            sol = list()
            sol.append([1])
            return sol
        elif numRows == 2:
            sol = list()
            sol.append([1])
            sol.append([1,1])
            return sol
        elif numRows > 2:
            sol = list()
            sol.append([1])
            sol.append([1,1])

            # GENERAR EL VECTOR DEL SIGUIENTE NIVEL
            for i in range(numRows-2):
                #print("Vector a tratar:")
                #print(sol[i+1])
                new_vector = list()# VECTOR QUE ALMACENA LA SOLUCION
                new_vector.append(1)
                length_new_vector = len(sol[i+1])
                #print("leng::::: {}".format(length_vector_analisis))
                for element in range(length_new_vector-1):# CALCULO DE LA SUMA DE LOS 2 NUMEROS
                    # numRows = 4 - 2 = 2 , Element = 0, 1, 2
                    #print("{} + {}".format(sol[i+1][element], sol[i+1][element+1]))
                    calc = sol[i+1][element] + sol[i+1][element+1]
                    new_vector.append(calc)


                new_vector.append(1)
                #print("NV::: {}".format(new_vector))
                sol.append(new_vector)

            print("return type::::::  {}".format(type(sol)))
            return sol
                
        else:
            sol = list()
            return sol
            


def run():
    pascal_triangle = Solution()
    sol_pascal_triangle = pascal_triangle.generate(18)
    print("Solution to send:::")
    print(sol_pascal_triangle)
    print("<Type of solution::::::::::::::::::: {}".format(type(sol_pascal_triangle)))
    
    for vector in sol_pascal_triangle:
        print(vector)

if __name__ == '__main__':
    run()

"""

SUCCESS     Details:

Runtime:        24 ms,   faster than     12.47%  of Python online submissions for Pascal's Triangle.
Memory Usage:   13.7 MB  less than       11.47%  of Python online submissions for Pascal's Triangle.

"""
