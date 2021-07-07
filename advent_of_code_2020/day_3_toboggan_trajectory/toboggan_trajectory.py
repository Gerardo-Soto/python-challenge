"""

--- Day 3: Toboggan Trajectory ---
With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

"""
import pdb

def run(x,y):
    print("Welcome.")
    file_name = "input.txt"
    print("Opening the file: {}".format(file_name))
    try:
        trajectory = open(file_name,"rt")
    except IOError:
        print("Error: File {} doesnt exists.")
        return 0

    axis_x = 0
    count_trees = 0
    #print(len(trajectory))

    count = 0
    length_line = 31
    for line in trajectory:
        print("{}".format(line))
        #count += 1
        print("{}^".format("*"*(axis_x % length_line)))
        print("p:{} c:{}  n_line:{}".format(axis_x % length_line,line[axis_x % length_line],count))

        if (line[(axis_x % 31)] == '#') and (count % y == 0):
            print("FOUND IT!!!  x:{}   line:{}".format(axis_x % length_line,count))
            print("{} pos: {}, char: {}".format(line,(axis_x % length_line),line[axis_x % length_line]))
            print("{}^".format("*"*(axis_x % length_line)))
            print("0{}{}{}".format("-"*10,"+"*10,"="*10))
            count_trees += 1
        #    axis_x += x
        else:
            pass
        
        if (count % y == 0):
            axis_x += x
        
        count += 1
        #axis_x += x
#        pdb.set_trace()

    print("Trees # Found::: {}".format(count_trees))
    return(count_trees)    



if __name__ == '__main__':
    first_problem = run(3,1)# 203
#    print(first_problem)
    second_problem = run(1,1)# 68
#    print(second_problem)
    trird_problem = run(5,1)# 78
    fourth_problem = run(7,1)# 77
    fifth_problem = run(1,2)# 36    v2: 40
    print("Solution of the second problem::: {}".format(first_problem * second_problem * trird_problem * fourth_problem * fifth_problem))

"""

Time Start:     18-dic-2020     14:31
Time End:       19-dic-2020     21:00


trys:   72 XXXXXXXXXX
        75 xxxxxxxxxxxx
        203  oooooooooooo

sol_2
trys:   2984645664   <- is to low

Good:   3316272960
"""
