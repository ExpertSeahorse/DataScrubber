import re
import random
acct = re.compile(r'(\d{16}\s)')
name = []

with open('celebraties.txt', 'r') as names:
    for i in names:
        name.append(i.rstrip())


with open('BC460-Cloned.txt') as fin:
    with open('OUTPUT.txt', 'w') as fout:
        for line in fin:
            if acct.match(line):
                new_name = random.choice(name).upper()
                if len(new_name) > 18:
                    new_name = new_name[:18]
                elif len(new_name) < 18:
                    new_name = new_name.ljust(18)
                mine = line[:18] + new_name + line[40:]
                fout.write(mine)
            else:
                fout.write(line)
