import re
import random
body = re.compile(r'\s\d{4}-\d{4}-\d{4}-\d{4}\s')
name = []


def acctnum():
    a1 = str(random.randint(1000, 9999))
    a2 = str(random.randint(1000, 9999))
    a3 = str(random.randint(1000, 9999))
    a4 = str(random.randint(1000, 9999))
    a5 = a1 + '-' + a2 + '-' + a3 + '-' + a4
    return a5


def homenum():
    h1 = str(random.randint(100, 999))
    h2 = str(random.randint(1000000, 9999999))
    return h1 + '-' + h2


def buisnum():
    b1 = str(random.randint(100, 999))
    b2 = str(random.randint(1000000, 9999999))
    return b1 + '-' + b2


def plasdate():
    p1 = str(random.randint(1, 12))
    if len(p1) < 2:
        p1 = '0' + p1
    p2 = str(random.randint(1, 31))
    if len(p2) < 2:
        p2 = '0' + p2
    p3 = str(random.randint(0, 25))
    if len(p3) < 2:
        p3 = '0' + p3
    return p1 + "/" + p2 + "/" + p3


def prevdate():
    prev1 = str(random.randint(1, 12))
    if len(prev1) < 2:
        prev1 = '0' + prev1
    prev2 = str(random.randint(2000, 2019))
    return prev1 + "/" + prev2

def rptdays():
    return str(random.randint(100, 999))


def new_name():
    name2 = random.choice(name).upper()
    if len(name2) > 22:
        return new_name[:22]
    elif len(name2) < 22:
        return name2.ljust(22)


with open('celebraties.txt', 'r') as names:
    for i in names:
        name.append(i.rstrip())


with open('BC460-Cloned.txt') as fin:
    with open('OUTPUT.txt', 'w') as fout:
        for line in fin:
            if body.match(line):

                mine = line[0] + acctnum() + line[20:22] + new_name() + line[44:49] +\
                       homenum() + line[60:62] + buisnum() + line[73:75] + plasdate() + line[83:87] + prevdate() +\
                       line[94:118] + rptdays() + line[121:]
                fout.write(mine)
            else:
                fout.write(line)
