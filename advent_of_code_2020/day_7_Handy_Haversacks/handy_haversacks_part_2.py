"""

--- Day 7: Handy Haversacks ---

--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
*
Util:

https://www.python-course.eu/graphs_python.php
https://www.youtube.com/watch?v=TtXI3OU1Od0
"""

import datetime

class Rules():
    def __init__(self, file_name):
        self.file_name = file_name
        self.content = None
        
    def load_file(self):
        try:
#            file_name = "input.txt"
            self.content = open(self.file_name, "r")
        except (FileNotFoundError, IOError) as file_error:
            print(f"Error file: {file_error}")
            exit()
        else:
            print(f"File {self.file_name} loaded.")
        finally:
            print(f"Next step: Creating tree.")

    def creating_tree(self, search_bag):
        print(f"Content of {self.file_name}:")
        bags_dict = dict()
        for line in self.content:
            #print(f"{line}")
            values_bag_tuto = []
            #key_bag = line.replace(' no other bags.', '.')
            key_bag = line.replace('bags.', '')
            key_bag = key_bag.replace('bags', '')
            key_bag = key_bag.replace('bag', '')
            key_bag = key_bag.replace('.', '')
            key = key_bag.split('contain ')[0]
            key = key.rstrip()
            values_bag = key_bag.split('contain ')[1]
            values_bag = values_bag.split(", ")
            #print(f":::::::::::{values_bag}")
            for value in values_bag:
                value_number = value.split(' ', 1)[0]
                value_name = value.split(' ', 1)[1]
                value_name = value_name.split(' \n')[0]
                value_name = value_name.rstrip()
                values_bag_tuto.append([value_number, value_name])
            
            bags_dict[key] = values_bag_tuto

        for key, value in bags_dict.items():
            print(f"k:'{key}' - v:{str(value)}")

        """found = False
        current_bag = search_bag

        whi<le not found:"""
        print(f"Bag to test: {search_bag}")
        print("")
        total = 0

        for rule in bags_dict:
            bags_sol = [rule]
            print(f"bags_sol::: {bags_sol}")
            while len(bags_sol) > 0:
                print(f"¿bags_sol[0]:: {bags_sol[0]} IN bags_dict::: {bags_dict}" )
                if bags_sol[0] in bags_dict:
                    """ What do? """
                    print("for new_bag IN bags_dict[bags_sol[0]]::: {bags_dict[bags_sol[0]]}")
                    for new_bag in bags_dict[bags_sol[0]]:
                        if new_bag[1] not in bags_sol:
                            bags_sol.append(new_bag[1])

                del bags_sol[0]
                if "shiny gold" in bags_sol:
                    print(f"bags_sol: {bags_sol} - total: {total} +1")
                    total += 1
                    break

        print(f"Solution::: {str(total)}")
            


if __name__ == '__main__':
    print("Welcome!")
    sol = Rules("input.txt")
    sol.load_file()
    search_bag = input("Enter the color bag:::")
    sol.creating_tree(search_bag)
