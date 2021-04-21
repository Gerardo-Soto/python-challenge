""""""

class Soluction(object):
    def findLenghtOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        flag = 0
        first = False
        count = 0
        for element in arr:
            print("e: {}  -  f: {}".format(element, flag))
            if first:
                if element >= flag:
                    flag = element
                else:
                    count += 1
            else:
                first = True
                flag = element

            print("c: {}".format(count))

        return count

    def is_shorted(self, arr):
        first_element = True
        length_arr = len(arr)
        for i_element in range(arr-1):
            if arr[i_element] <= arr[i_element+1]:
                pass
            else:
                return False
        return True


    def third_sol_binary(self, arr):
        import re
#        is_shorted = 0
        length_arr = len(arr)
        print("--------------START-------------")
        #print(length_arr)
        max_length = 0
        array_to_eval = list()
        list_of_soluction = dict()
        length_sol = 0
        is_perfect = 0
        for i in range(length_arr-1):
            if arr[i] <= arr[i+1]:
                is_perfect += 1

        if is_perfect == length_arr-1:
#            print("Array perfect ----------")
            return 0

        for i in range(2**length_arr):
            #print("number: {}".format(i))
            a = str(bin(i)[2:].zfill(length_arr+2))
            a = a[2::]
            #print(a)
            re_sol = re.search("^1*0+1*$",a)
            if re_sol:
                #print("Sol Val++++++++ ::::::: {}".format(a))

            #print(arr)
            #print(a)
            #print("a[6]: {}".format(a[6]))
            #--->
                array_to_eval.clear()
                for j in range(length_arr):
                
                    if (int(a[j]) == 1):
                        array_to_eval.append(arr[j])

                len_array_to_eval = len(array_to_eval)
                #print("Array to eval::: {}   ++++++++++++++ len: {} - Sol: {}".format(array_to_eval,len_array_to_eval,length_arr - len_array_to_eval))
                new_length = len(array_to_eval)

                is_shorted = 0
                is_perfect = 0
                for i_element in range(new_length-1):
                    if array_to_eval[i_element] <= array_to_eval[i_element+1]:
                        pass
                    else:
                        is_shorted += 1

                if is_shorted == 0:
                    #print("ARRAY SHORTED::: {}   !!!!!!!!!!!!!!!!!".format(array_to_eval))
                    if new_length >= max_length:
                        max_length = new_length
                        length_sol = length_arr - max_length
                    else:
                        pass

                    #print("Solución valida::::::: {}    len: {} - Sol: {}".format(array_to_eval,new_length,length_arr - new_length))
###                    print("Array shorted::: {} - len-Sol: {}  *****".format(array_to_eval,length_sol))
                else:
                    pass

            else:
                pass
        print("RETURN::::: {}".format(length_sol))
        return int(length_sol)


def run():
    print("Welcome.")
#    arr = [1,2,3,10,4,2,3,5] # Sol: 3
#    arr = [5,4,3,2,1] # Sol: 4
#    arr = [1,2,3] # Sol: 0
#    arr = [13,0,14,7,18,18,18,16,8,15,20] # Sol: 8
    arr = [1,2,3,10,4]
    print("Array to analize::: {}   length::: {}".format(arr,len(arr)))
    sol = Soluction()
    #print(sol.findLenghtOfShortestSubarray(arr))
    #print(sol.second_sol(arr))
    print("Sol::::::::: {}".format(sol.third_sol_binary(arr)))


if __name__ == '__main__':
    run()
