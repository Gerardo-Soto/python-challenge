import os


def run():
    print("Opening the file:")
    numbers = open("expense_report.txt","rt")
    list_numbers = list()
    for number in numbers:
        #print("{}".format(number))
        list_numbers.append(int(number))
        
    #print(list_numbers)
    length_numbers = len(list_numbers)
    for i in range(length_numbers-1):
        for j in range(i+1, length_numbers):
            if (list_numbers[i] + list_numbers[j] == 2020):
                print("Found it!!!!!!")
                print("{} & {} = {}".format(list_numbers[i],list_numbers[j],(list_numbers[i]+list_numbers[j])))
                print("Sol::::::::::::: {}".format(list_numbers[i]*list_numbers[j]))
            else:
                pass


    for num in list_numbers:
        
        
        #print(num)
        toFind = 2020 - num
        
        if (toFind in list_numbers):
            print("Found It!!!!!! ::: {}".format(num * toFind))

    for i in range(length_numbers-2):
        for j in range(i+1, length_numbers-1):
            toFind = 2020 - list_numbers[i] - list_numbers[j]
            
            if (toFind in list_numbers):
                print("\nPart two~~~~~~".format())
                print("Found it!!!!!! ::: {} + {} + {} = 2020".format(list_numbers[i],list_numbers[j],toFind))
                print("Sol::: {}".format(list_numbers[i]*list_numbers[j]*toFind))
#               return 0

if __name__ == '__main__':
    run()
