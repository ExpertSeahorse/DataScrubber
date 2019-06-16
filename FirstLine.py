import re
import random
first_line = re.compile(r'.\w{3}#\s\w{2}\d{3}-\d{2}')


def new_date():
    d1 = str(random.randint(1, 12))
    if len(d1) < 2:
        d1 = '0' + d1
    d2 = str(random.randint(1, 31))
    if len(d2) < 2:
        d2 = '0' + d2
    d3 = str(random.randint(0, 25))
    if len(d3) < 2:
        d3 = '0' + d3
    return d1 + "/" + d2 + "/" + d3


def corp():
    return str(random.randint(100000, 999999))


def inst():
    return str(random.randint(100000, 999999))

def assn():
    assn_num = str(random.randint(0, 99))
    if len(assn_num) < 2:
        assn_num = '0' + assn_num
    return assn_num


with open('BC460-Cloned.txt') as fin:
    with open('OUTPUT.txt', 'w') as fout:
        for line in fin:
            if first_line.match(line):
                mine = line[:24] + assn() + line[26:33] + corp() + line[39:46] + inst() + line[52:106] + new_date() + line[114:]
                fout.write(mine)
            else:
                fout.write(line)
