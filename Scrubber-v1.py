from FirstLine import *
from SecondLine import *
from Body import *

with open('BC460-Cloned.txt') as fin:
    with open('OUTPUT.txt', 'w') as fout:
        for line in fin:
            if first_line.match(line):
                mine = line[:24] + assn() + line[26:33] + corp() + line[39:46] + \
                       inst() + line[52:106] + new_date() + line[114:]

                fout.write(mine)
            elif second_line.match(line):
                mine = line[:4] + bin_num() + line[10:105] + run_date() + line[113:]

                fout.write(mine)
            elif body.match(line):
                mine = line[0] + acctnum() + line[20:22] + new_name() + line[44:49] +\
                       homenum() + line[60:62] + buisnum() + line[73:75] + plasdate() + line[83:87] + prevdate() +\
                       line[94:118] + rptdays() + line[121:]

                fout.write(mine)
            else:
                fout.write(line)
