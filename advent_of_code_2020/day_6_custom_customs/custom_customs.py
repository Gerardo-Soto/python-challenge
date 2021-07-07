"""

--- Day 6: Custom Customs ---
As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz
In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

The first group contains one person who answered "yes" to 3 questions: a, b, and c.
The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
The last group contains one person who answered "yes" to only 1 question, b.
In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

"""
import datetime


class QuestionsAnswers:
    def load_file(self):
        try:
            file_name = "input.txt"
            content = open(file_name, "r")
        except (FileNotFoundError, IOError) as file_error:
            print(f"Error 1: {file_error}")
            exit()
        else:
            print(f'File {file_name} loaded.')
        finally:
            print("Next step.")

        lines = content.readlines()
        content.close()

        groups_list = list()
        answers_by_group = set()
        answers_yes = 0

        for line in lines:
            if line == "\n":
                #print(f"n {line}")
                if len(answers_by_group) == 0:
                    pass
                else:
                    groups_list.append(answers_by_group)
                    #print(f"Set::: {answers_by_group} \t Answers: {len(answers_by_group)}")
                    answers_yes += len(answers_by_group)
                    answers_by_group.clear()

            else:
                #print(f"  {line}---")
                for letter in line:
                    if letter == "\n":
                        pass
                    else:
                        answers_by_group.add(letter)

        groups_list.append(answers_by_group)
        answers_yes += len(answers_by_group)
        answers_by_group.clear()
            
        print(f"Solution 1 ::: {answers_yes}")


if __name__ == '__main__':
    count_question = QuestionsAnswers()
    count_question.load_file()


"""
Start       30-12-2020  18:50
End         30-12-2020  19:41       00:51



Sol     7020    xxxxx       Is too low.
Sol     7027    ooooooooooooooooooooooooooo

"""
