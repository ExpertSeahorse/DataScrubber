import re
import random
date = re.compile(r'.\w{3}#\s\w{2}\d{3}-\d{2}')

with open('BC460-Cloned.txt') as fin:
    with open('OUTPUT.txt', 'w') as fout:
        for line in fin:
            if date.match(line):
                r1 = str(random.randint(1, 12))
                if len(r1) < 2:
                    r1 = '0' + r1
                r2 = str(random.randint(1, 31))
                if len(r2) < 2:
                    r2 = '0' + r2
                r3 = str(random.randint(0, 25))
                if len(r3) < 2:
                    r3 = '0' + r3

                new_date = '    ' + r1 + "/" + r2 + "/" + r3
                mine = line[:97] + 'AS OF' + new_date + line[114:]
                fout.write(mine)
            else:
                fout.write(line)
