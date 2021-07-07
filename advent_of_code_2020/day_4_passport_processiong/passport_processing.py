"""

--- Day 4: Passport Processing ---
You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

"""
import datetime

def run():
    print("Wellcome!")
    passport_list = list()
    passport_dict = dict()
    try:
        contents = open("input.txt","r")
    except (FileNotFoundError, IOError):
        print("Error.")

    lines = contents.readlines()
    print(type(lines))
    contents.close()

    start = datetime.datetime.now()

    for line in lines:
        if line == "\n":
#            print("--------EMPTY LINE")
            ## si hay algo en el dict, guardalo
            
            if passport_dict:
#                print("Passport: {}".format(passport_dict))
                passport_list.append(passport_dict)
                del passport_dict
                passport_dict = dict()
            else:
#                print("New passport...")
                passport_dict = dict()

        else:
            
            line = line.replace("\n","")
            fields = line.split(" ")
            #print(fields)
            for field in fields:
                key, value = field.split(":")
 #               print("key: {} - value: {}".format(key,value))
                passport_dict[key] = value

    passport_list.append(passport_dict)
    
    passports_valid = 0
    passports_invalid = 0
    for passport in passport_list:
#        print(type(passport))
        iyr = passport.get("iyr")
        hgt = passport.get("hgt")
        hcl = passport.get("hcl")
        byr = passport.get("byr")
# Cid = Null is valid
#        cid = passport.get("cid")
        pid = passport.get("pid")
        eyr = passport.get("eyr")
        ecl = passport.get("ecl")
        if iyr and hgt and hcl and byr and pid and eyr and ecl:
            #if (2010 <= int(iyr) <= 2020) and hgt and hcl and (1920 <= int(byr) <=2002 ) and pid and (2020 <= int(eyr) <= 2030) and ecl:
#            print("Passport valid!!!")
            passports_valid += 1
        else:
#            print("Passport ERROR...")
            passports_invalid += 1

    end = datetime.datetime.now()

    print("Passports valids::::::  {}".format(passports_valid))
    print("Passport Not valids:::  {}".format(passports_invalid))

    print("Running time::: {}".format(end-start))
    """    print("All passports:::")
    print(passport_list)
    """


if __name__ == '__main__':
    run()

"""
Solution::: 210 Passports valid.
             66 Passports NOT valid.

"""
