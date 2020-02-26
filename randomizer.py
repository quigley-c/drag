import sys
import random

def main(input_params):
    """"""
    chars = read_characters(input_params[1])

    charlist = chars[0].strip().split(",")
    forall = chars[1].strip().split(",")
    special = chars[2].strip().split(",")

    int(input_params[2])
    choices = pick_random(charlist, int(input_params[2]))
    print_choices(choices)
#

def read_characters(filepath):
    """"""
    try:
        f = open(filepath, "r")
        f.mode == "r"
        chars = f.read().strip().split("\n")
        return chars
    except:
        print("Couldn't open file. Please make sure file exists and that you are providing the correct path.")
#

def pick_random(charlist, n):
    """"""
    charrange = int(len(charlist) / n)
    choices = []
    for i in range(n):
        new = []
        for j in range(charrange):
            index = random.choice(charlist)
            new.append(index)
            charlist.remove(index)
        choices.append(new)

    return choices
#

def print_choices(choices):
    for i in range(len(choices)):
        print("Player ", i+1, "\n--------")
        for j in range(len(choices[i])):
            print(choices[i][j])
        print("")
#

if __name__ == "__main__":
    main(sys.argv)
