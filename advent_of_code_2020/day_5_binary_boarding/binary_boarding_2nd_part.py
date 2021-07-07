"""

--- Day 5: Binary Boarding ---
You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.

You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.
So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

"""

import datetime

class BinaryBoarding:
    def __init__(self, file_name):
        self.file_name = file_name


    def run(self):
        print("Welcome!")

    def read_file(self, file_name):
        self.data = open(file_name,"r")

    def solution_binary(self):
        #print(self.data)
        seat_id_max = 0
        seats_list = list()
        for word in self.data:
            #print(word)
            row = []
            column = []
            count_delimiter = 0
            
            for letter in word:
                if count_delimiter < 7:
                    if letter == 'F':
                        row.append(0)
                    elif letter == 'B':
                        row.append(1)

                else:
                    if letter == 'L':
                        column.append(0)
                    elif letter == 'R':
                        column.append(1)
                
                count_delimiter += 1

            count_delimiter = 0
            row_dec = 0
            for b in row:
                row_dec = 2 * row_dec + b

            column_dec = 0
            for b in column:
                column_dec = 2 * column_dec + b

            seat_id_cal = (row_dec * 8) + column_dec
            #print("row: {} - col: {}".format(row, column))
            #print("r:{} - c:{} - id:{}".format(row_dec, column_dec, seat_id_cal))
            seats_list.append(seat_id_cal)
            if seat_id_max < seat_id_cal:
                seat_id_max = seat_id_cal

        seats_list.sort()
        print(seats_list)
        n = 0
        l = len(seats_list)
        print(l)
        for i in range(48,819):
            if i == seats_list[n]:
                n += 1
            else:
                print("Without ID!!!!!!! {} - {}".format(i,seats_list[n]))

                n += 0
        return seat_id_max


if __name__ == '__main__':
    sol = BinaryBoarding(file_name = "input.txt")
    print(type(sol))
    sol.run()
    try:
        start_1 = datetime.datetime.now()
        sol.read_file(file_name = "input.txt")
        end_1 = datetime.datetime.now()
    except FileNotFoundError:
        print("Error: {}".format(FileNotFoundError))
    finally:
        start_2 = datetime.datetime.now()
        answer = sol.solution_binary()
        print("Solution: {}".format(answer))
        end_2 = datetime.datetime.now()
        print("Time of load file::: {}".format(end_1 - start_1))
        print("Time of solution:::: {}".format(end_2 - start_2))
    

"""
Time of load file:  0.0029 s
Time of solution::  0.0196 s

Solución 2 :::      ID: 559
"""
