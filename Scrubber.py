import re
acct = re.compile(r'^(?P<cid>\d{16})')
li = []

with open('BC460-Cloned.txt') as fin:
    rin = fin.read()
    with open('OUTPUT.txt') as fout:
        wout = fout.write()
    # sread = read.strip()
    # Removes all hyphens from text
        for index, line in enumerate(rin):
            if index > 257:
                # line = line.lstrip()
                for character in line:
                    if character != '-':
                        li.append(character)
            elif index <= 256 or 450 <= index < 500:
                pass

        '''for character in line:
            if character != '-':
                li.append(character)'''


    interm_doc= ''.join(li)
    print(interm_doc)

    # Will check for acct numbers

    # print(re.findall(acct, new_doc))
