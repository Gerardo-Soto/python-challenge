"""

--- Day 8: Handheld Halting ---
Your flight to the major airline hub reaches cruising altitude without incident. While you consider checking the in-flight menu for one of those drinks that come with a little umbrella, you are interrupted by the kid sitting next to you.

Their handheld game console won't turn on! They ask if you can take a look.

You narrow the problem down to a strange infinite loop in the boot code (your puzzle input) of the device. You should be able to fix it, but first you need to be able to run the code in isolation.

The boot code is represented as a text file with one instruction per line of text. Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).

acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
For example, consider the following program:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
These instructions are visited in this order:

nop +0  | 1
acc +1  | 2, 8(!)
jmp +4  | 3
acc +3  | 6
jmp -3  | 7
acc -99 |
acc +1  | 4
jmp -4  | 5
acc +6  |
First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1 (acc +1) and jmp +4 sets the next instruction to the other acc +1 near the bottom. After it increases the accumulator from 1 to 2, jmp -4 executes, setting the next instruction to the only acc +3. It sets the accumulator to 5, and jmp -3 causes the program to continue back at the first acc +1.

This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program tries to run any instruction a second time, you know it will never terminate.

Immediately before the program would run an instruction a second time, the value in the accumulator is 5.

Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?


PART 2

--- Part Two ---
After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6
After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?

"""
#-*- coding:utf-8 -*-

import datetime

class HandheldGame:
    """Class to solution the boot code."""
    def __init__(self, file_name):
        """Constructor method:   """
        self.file_name = file_name
        self.content = None


    def loadFile(self):
        """"""
        try:
            self.content = open(self.file_name, 'r')
        except (FileNotFoundError, IOError) as file_error:
            print(f'Error file: {file_error}')
            exit()
        else:
            print(f'File {file_name} loaded.')
        finally:
            print('Next step.')


    def solution(self):
        """"""
        print(f'This is the content to {self.file_name} for solution:::')
        list_instructions = list()
        for line in self.content:
            if line is not '\n':
                dict_instruction = dict()
                info_instruction = line.split(' ')
                info_instruction[1] = info_instruction[1].replace('\n', '')
                dict_instruction[info_instruction[0]] = info_instruction[1]
                dict_instruction['visited'] = False
                list_instructions.append(dict_instruction)

        print(f'Lines of file::: {len(list_instructions)}')

#        for dict_inst in list_instructions:
#            print(dict_inst)
#            print(list(dict_inst.keys())[0])

        print(f'Last dict::: {list_instructions[len(list_instructions) -1]}')

        #print(list(list_instructions[len(list_instructions) -1].keys())[0])
        if list(list_instructions[len(list_instructions) -1].keys())[0] == 'jmp':
            print('Error found it !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            list_instructions[len(list_instructions) -1]['nop'] = list_instructions[len(list_instructions) -1]['jmp']
            del list_instructions[len(list_instructions) -1]['jmp']

            del list_instructions[len(list_instructions) -1]['visited']
            list_instructions[len(list_instructions) -1]['visited'] = False



            
        print(f'new key::: {list(list_instructions[len(list_instructions) -1])}')

        print('\nTo work:\n')
        accumulator = 0
        second_time = 0
        position = 0

        current_values = list_instructions[0]
        current_key = current_values.keys()

        for key in current_key:
            current_key = key
            break

        
        print(f'k: {current_key},  v: {current_values[current_key]},  s:{current_values["visited"]}')
        while not second_time:
            if not current_values["visited"]:
                if position == (len(list_instructions) - 1):
                    second_time = True

                list_instructions[position]["visited"] = True
                #current_values = list_instructions[0]
                #print(f'{current_values} ------ ck: -{current_key}-')
                if current_key == 'nop':
                    print(f'key -{current_key}- : pass--->  position: {position} + 1 : & a: {accumulator} + 0')
                    position += 1
                    current_values = list_instructions[position]

                elif current_key == 'acc':
                    print(f'key -{current_key}- : acc----->  position: {position} + 1 & a: {accumulator} + {current_values[current_key]}')
                    position += 1
                    accumulator = accumulator + int(current_values[current_key])
                    current_values = list_instructions[position]

                else:
                    print(f'key -{current_key}- : jump---->  position: {position} + {current_values[current_key]} & a: {accumulator} + 0')
                    position += int(current_values[current_key])
                    current_values = list_instructions[position]


                current_values = list_instructions[position]
                current_key = current_values.keys()
                for key in current_key:
                    current_key = key
                    break

            else:
                second_time = True

        #print(f'the 5th instruction is::: {list_instructions[4]}')
        print(f'Solution::: {accumulator}')


if __name__ == '__main__':
    print('Welcome')
    file_name='input_2.txt'
    print(f'The file to load is: {file_name}')
    sol_handheld_game = HandheldGame(file_name)
    start_load = datetime.datetime.now()
    sol_handheld_game.loadFile()
    end_load = datetime.datetime.now()
    start_solution = datetime.datetime.now()
    sol_handheld_game.solution()
    end_solution = datetime.datetime.now()
    print(f'\nTime to load file::: {end_load - start_load}')
    print(f'Time to solution:::::: {end_solution - start_solution}')


"""
Start time: 8-feb-2021  17:23


Solution::::::::: 

"""
