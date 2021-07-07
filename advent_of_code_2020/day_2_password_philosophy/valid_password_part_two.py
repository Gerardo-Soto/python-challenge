"""
--- Day 2: Password Philosophy ---

--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""

def run():
    print("Opening the file:")
    passwords = open("input.txt","rt")
    list_passwords = list()
    password_valid = 0
    for password in passwords:
        #list_passwords.append(password.split(' '))
        list_info = password.split(' ')

        num_min_max = list_info[0].split('-')
        #print(num_min_max[0],num_min_max[1])

        character = list(list_info[1])
        
        password_to_be_analyzed = list_info[2]

        #occurrences = password_to_be_analyzed.count(character[0])
        #print(password_to_be_analyzed,character[0],occurrences)
        if (password_to_be_analyzed[int(num_min_max[0])-1] == character[0] and password_to_be_analyzed[int(num_min_max[1])-1] != character[0]):
            password_valid += 1
            print(num_min_max,character[0],password_to_be_analyzed)
        elif (password_to_be_analyzed[int(num_min_max[0])-1] != character[0] and password_to_be_analyzed[int(num_min_max[1])-1] == character[0]):
            password_valid += 1
            print(num_min_max, character[0], password_to_be_analyzed)
        else:
            pass

    print("Passwords Valid::: {}".format(password_valid))

    

if __name__ == '__main__':
    run()


"""
Success

Time start: 23:23
Time end:   23:43 

Time:   20 Min

"""
