# Extra sources:
# Reading from CSV - https://www.youtube.com/watch?v=5CEsJkKhS78

import sys
import csv


def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py DATABASE SEQUENCE")

    # Read sequence into a string
    with open(sys.argv[2]) as file:
        sequence = file.read()

    # Create a list with the STRs (only first row on csv file)
    with open(sys.argv[1]) as file:
        line = csv.reader(file)
        for row in line:
            STRs_list = row
            STRs_list.pop(0)  # remove 'name' column
            break
    # Make a dictionary with the list where the STRs are the keys
    STRs_Dict = {}
    for key in STRs_list:
        STRs_Dict[key] = 1

    # Iterate throught the DNA sequence and count any repetion of the dictionary values
    for STR in STRs_Dict:
        lenght = len(STR)
        repMax = 0
        rep = 0
        for i in range(len(sequence)):
            while rep > 0:
                rep -= 1
                continue
            if sequence[i: i + lenght] == STR:
                while sequence[i - lenght: i] == sequence[i: i + lenght]:
                    rep += 1
                    i += lenght
                if rep > repMax:
                    repMax = rep
        STRs_Dict[STR] += repMax

    # Compare count with the database
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for person in reader:
            match = 0
            for str_count in STRs_Dict:
                if STRs_Dict[str_count] == int(person[str_count]):
                    match += 1
            if match == len(STRs_Dict):
                print(person['name'])
                exit()
        print("No match")


if __name__ == "__main__":
    main()