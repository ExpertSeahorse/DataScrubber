import re
import datetime
import random
second_line = re.compile(r'BIN \d{6}\s')


def run_date():
    date = datetime.datetime.now()
    return str(date.month) + "/" + str(date.day) + "/" + str(date.year)


def bin_num():
    return str(random.randint(100000, 999999))


with open('BC460-Cloned.txt') as fin:
    with open('OUTPUT.txt', 'w') as fout:
        for line in fin:
            if second_line.match(line):
                mine = line[:4] + bin_num() + line[10:105] + run_date() + line[113:]
                fout.write(mine)
            else:
                fout.write(line)   
